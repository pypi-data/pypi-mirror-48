"""CLI module.

This module contains the CLI for repobee.

.. module:: cli
    :synopsis: The CLI for repobee.

.. moduleauthor:: Simon Larsén
"""

import argparse
import requests
import pathlib
import os
import sys
import re
from contextlib import contextmanager
from typing import List, Iterable, Optional, Tuple

import logging
import daiquiri

import repobee_plug as plug

import repobee
from repobee import command
from repobee import github_api
from repobee import gitlab_api
from repobee import util
from repobee import tuples
from repobee import exception
from repobee import config
from repobee import apimeta

daiquiri.setup(
    level=logging.INFO,
    outputs=(
        daiquiri.output.Stream(
            sys.stdout,
            formatter=daiquiri.formatter.ColorFormatter(
                fmt="%(color)s[%(levelname)s] %(message)s%(color_stop)s"
            ),
        ),
        daiquiri.output.File(
            filename="{}.log".format(__package__),
            formatter=daiquiri.formatter.ColorFormatter(
                fmt="%(asctime)s [PID %(process)d] [%(levelname)s] "
                "%(name)s -> %(message)s"
            ),
        ),
    ),
)


def _filter_tokens():
    """Filter out any secure tokens from log output."""
    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.msg = re.sub("https://.*?@", "https://", record.msg)
        return record

    logging.setLogRecordFactory(record_factory)


_filter_tokens()

LOGGER = daiquiri.getLogger(__file__)
SUB = "subparser"

# Any new subparser mus tbe added to the PARSER_NAMES tuple!
SETUP_PARSER = "setup"
UPDATE_PARSER = "update"
CLONE_PARSER = "clone"
MIGRATE_PARSER = "migrate"
OPEN_ISSUE_PARSER = "open-issues"
CLOSE_ISSUE_PARSER = "close-issues"
LIST_ISSUES_PARSER = "list-issues"
VERIFY_PARSER = "verify-settings"
ASSIGN_REVIEWS_PARSER = "assign-reviews"
PURGE_REVIEW_TEAMS_PARSER = "purge-review-teams"
CHECK_REVIEW_PROGRESS_PARSER = "check-reviews"
SHOW_CONFIG_PARSER = "show-config"

PARSER_NAMES = (
    SETUP_PARSER,
    UPDATE_PARSER,
    CLONE_PARSER,
    MIGRATE_PARSER,
    OPEN_ISSUE_PARSER,
    CLOSE_ISSUE_PARSER,
    LIST_ISSUES_PARSER,
    VERIFY_PARSER,
    ASSIGN_REVIEWS_PARSER,
    PURGE_REVIEW_TEAMS_PARSER,
    SHOW_CONFIG_PARSER,
    CHECK_REVIEW_PROGRESS_PARSER,
)

# TODO Remove support for these deprecated parsers in 2.0
ASSIGN_REVIEWS_PARSER_OLD = "assign-peer-reviews"
PURGE_REVIEW_TEAMS_PARSER_OLD = "purge-peer-review-teams"
CHECK_REVIEW_PROGRESS_PARSER_OLD = "check-peer-review-progress"

DEPRECATED_PARSERS = {
    ASSIGN_REVIEWS_PARSER_OLD: tuples.Deprecation(
        replacement=ASSIGN_REVIEWS_PARSER, remove_by="v2.0.0"
    ),
    PURGE_REVIEW_TEAMS_PARSER_OLD: tuples.Deprecation(
        replacement=PURGE_REVIEW_TEAMS_PARSER, remove_by="v2.0.0"
    ),
    CHECK_REVIEW_PROGRESS_PARSER_OLD: tuples.Deprecation(
        replacement=CHECK_REVIEW_PROGRESS_PARSER, remove_by="v2.0.0"
    ),
}


def parse_args(
    sys_args: Iterable[str]
) -> (tuples.Args, Optional[github_api.GitHubAPI]):
    """Parse the command line arguments and initialize the GitHubAPI.

    Args:
        sys_args: A list of command line arguments.

    Returns:
        a tuples.Args namedtuple with the arguments, and an initialized
        GitHubAPI instance (or None of testing connection).
    """
    parser = _create_parser()
    args = parser.parse_args(_handle_deprecation(sys_args))

    if getattr(args, SUB) == SHOW_CONFIG_PARSER:
        return tuples.Args(subparser=SHOW_CONFIG_PARSER), None

    _validate_tls_url(args.github_base_url)

    # environment token overrides config
    token = os.getenv("REPOBEE_OAUTH") or (
        args.token if "token" in args else ""
    )

    if getattr(args, SUB) == VERIFY_PARSER:
        # quick parse for verify connection
        return (
            tuples.Args(
                subparser=VERIFY_PARSER,
                org_name=args.org_name,
                github_base_url=args.github_base_url,
                user=args.user,
                traceback=args.traceback,
                master_org_name=args.master_org_name
                if "master_org_name" in args
                else None,
                token=token,
            ),
            None,
        )
    elif getattr(args, SUB) == CLONE_PARSER:
        # only if clone is chosen should plugins be able to hook in
        plug.manager.hook.parse_args(args=args)

    api = _connect_to_api(
        args.github_base_url,
        token,
        args.org_name,
        args.user if "user" in args else None,
    )

    master_org_name = args.org_name
    if "master_org_name" in args and args.master_org_name is not None:
        master_org_name = args.master_org_name
    master_names = args.master_repo_names
    master_urls = _repo_names_to_urls(master_names, master_org_name, api)
    assert master_urls and master_names

    groups = _extract_groups(args)
    subparser = getattr(args, SUB)
    if subparser in [
        ASSIGN_REVIEWS_PARSER,
        CHECK_REVIEW_PROGRESS_PARSER,
        ASSIGN_REVIEWS_PARSER,
    ] and any([len(g.members) > 1 for g in groups]):
        raise exception.ParseError(
            "review commands do not currently support groups of students"
        )

    parsed_args = tuples.Args(
        subparser=subparser,
        org_name=args.org_name,
        master_org_name=args.master_org_name
        if "master_org_name" in args
        else None,
        github_base_url=args.github_base_url,
        user=args.user if "user" in args else None,
        master_repo_urls=master_urls,
        master_repo_names=master_names,
        students=_extract_groups(args),
        issue=util.read_issue(args.issue)
        if "issue" in args and args.issue
        else None,
        title_regex=args.title_regex if "title_regex" in args else None,
        traceback=args.traceback,
        state=args.state if "state" in args else None,
        show_body=args.show_body if "show_body" in args else None,
        author=args.author if "author" in args else None,
        num_reviews=args.num_reviews if "num_reviews" in args else None,
        token=token,
    )

    return parsed_args, api


def _validate_tls_url(url):
    """Url must use the https protocol."""
    if not url.startswith("https://"):
        raise exception.ParseError(
            "unsupported protocol in {}: "
            "for security reasons, only https is supported".format(url)
        )


def _handle_deprecation(sys_args: List[str]) -> List[str]:
    """If the first argument on the arglist is a deprecated command, replace it
    with the corresponding current command and issue a warning.

    Returns:
        The sys_args list with any deprecated command replaced with the current
        one.
    """
    if not sys_args:
        return []

    parser_name = sys_args[0]
    if parser_name in DEPRECATED_PARSERS:
        deprecation = DEPRECATED_PARSERS[parser_name]
        LOGGER.warning(
            "use of '{}' has been deprecated and will be removed by {}, "
            "use '{}' instead".format(
                parser_name, deprecation.remove_by, deprecation.replacement
            )
        )
        return [deprecation.replacement] + sys_args[1:]

    return list(sys_args)


def dispatch_command(args: tuples.Args, api: github_api.GitHubAPI):
    """Handle parsed CLI arguments and dispatch commands to the appropriate
    functions. Expected exceptions are caught and turned into SystemExit
    exceptions, while unexpected exceptions are allowed to propagate.

    Args:
        args: A namedtuple containing parsed command line arguments.
        api: An initialized GitHubAPI instance.
    """
    if args.subparser == SETUP_PARSER:
        with _sys_exit_on_expected_error():
            command.setup_student_repos(
                args.master_repo_urls, args.students, api
            )
    elif args.subparser == UPDATE_PARSER:
        with _sys_exit_on_expected_error():
            command.update_student_repos(
                args.master_repo_urls, args.students, api, issue=args.issue
            )
    elif args.subparser == OPEN_ISSUE_PARSER:
        with _sys_exit_on_expected_error():
            command.open_issue(
                args.issue, args.master_repo_names, args.students, api
            )
    elif args.subparser == CLOSE_ISSUE_PARSER:
        with _sys_exit_on_expected_error():
            command.close_issue(
                args.title_regex, args.master_repo_names, args.students, api
            )
    elif args.subparser == MIGRATE_PARSER:
        with _sys_exit_on_expected_error():
            command.migrate_repos(args.master_repo_urls, api)
    elif args.subparser == CLONE_PARSER:
        with _sys_exit_on_expected_error():
            command.clone_repos(args.master_repo_names, args.students, api)
    elif args.subparser == VERIFY_PARSER:
        with _sys_exit_on_expected_error():
            github_api.GitHubAPI.verify_settings(
                args.user,
                args.org_name,
                args.github_base_url,
                args.token,
                args.master_org_name,
            )
    elif args.subparser == LIST_ISSUES_PARSER:
        with _sys_exit_on_expected_error():
            command.list_issues(
                args.master_repo_names,
                args.students,
                api,
                state=args.state,
                title_regex=args.title_regex or "",
                show_body=args.show_body,
                author=args.author,
            )
    elif args.subparser == ASSIGN_REVIEWS_PARSER:
        with _sys_exit_on_expected_error():
            command.assign_peer_reviews(
                args.master_repo_names,
                args.students,
                args.num_reviews,
                args.issue,
                api,
            )
    elif args.subparser == PURGE_REVIEW_TEAMS_PARSER:
        with _sys_exit_on_expected_error():
            command.purge_review_teams(
                args.master_repo_names, args.students, api
            )
    elif args.subparser == SHOW_CONFIG_PARSER:
        with _sys_exit_on_expected_error():
            command.show_config()
    elif args.subparser == CHECK_REVIEW_PROGRESS_PARSER:
        with _sys_exit_on_expected_error():
            command.check_peer_review_progress(
                args.master_repo_names,
                args.students,
                args.title_regex,
                args.num_reviews,
                api,
            )
    else:
        raise exception.ParseError(
            "Illegal value for subparser: {}. "
            "This is a bug, please open an issue.".format(args.subparser)
        )


def _add_peer_review_parsers(base_parsers, subparsers):
    assign_parser = subparsers.add_parser(
        ASSIGN_REVIEWS_PARSER,
        description=(
            "For each student repo, create a review team with pull access "
            "named <student>-<master_repo_name>-review and randomly assign "
            "other students to it. All students are assigned to the same "
            "amount of review teams, as specified by `--num-reviews`. Note "
            "that `--num-reviews` must be strictly less than the amount of "
            "students."
        ),
        help="Randomly assign students to peer review each others' repos.",
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    assign_parser.add_argument(
        "-n",
        "--num-reviews",
        metavar="N",
        help="Assign each student to review n repos (consequently, each repo "
        "is reviewed by n students). n must be strictly smaller than the "
        "amount of students.",
        type=int,
        default=1,
    )
    assign_parser.add_argument(
        "-i",
        "--issue",
        help=(
            "Path to an issue to open in student repos. If specified, this "
            "issue will be opened in each student repo, and the body will be "
            "prepended with user mentions of all students assigned to review "
            "the repo. NOTE: The first line is assumed to be the title."
        ),
        type=str,
    )
    subparsers.add_parser(
        PURGE_REVIEW_TEAMS_PARSER,
        description="Remove review teams assigned with `assign-peer-reviews`",
        help="Remove all review teams associated with the specified "
        "students and master repos.",
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    check_review_progress = subparsers.add_parser(
        CHECK_REVIEW_PROGRESS_PARSER,
        description=(
            "Check which students have opened review review issues in their "
            "assigned repos. As it is possible for students to leave the peer "
            "review teams on their own, the command checks that each student "
            "is assigned to the expected amound of teams. There is currently "
            "no way to check if students have been swapped around, so using "
            "this command fow grading purposes is not recommended."
        ),
        help=(
            "Fetch all peer review teams for the specified student repos, and "
            "check which assigned reviews have been done (i.e. which issues "
            "have been opened)."
        ),
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    check_review_progress.add_argument(
        "-r",
        "--title-regex",
        help=(
            "Regex to match against titles. Only issues matching this regex "
            "will count as review issues."
        ),
        required=True,
    )
    check_review_progress.add_argument(
        "-n",
        "--num-reviews",
        metavar="N",
        help=(
            "The expected amount of reviews each student should be assigned "
            "to perform. If a student is not assigned to `num_reviews` "
            "review teams, warnings will be displayed."
        ),
        type=int,
        required=True,
    )


def _add_issue_parsers(base_parsers, subparsers):
    open_parser = subparsers.add_parser(
        OPEN_ISSUE_PARSER,
        description=(
            "Open issues in student repositories. For each master repository "
            "specified, the student list is traversed. For every student repo "
            "found, the issue specified by the `--issue` option is opened. "
            "NOTE: The first line of the issue file is assumed to be the "
            "issue title!"
        ),
        help="Open issues in student repos.",
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    open_parser.add_argument(
        "-i",
        "--issue",
        help="Path to an issue. The first line is assumed to be the title.",
        type=str,
        required=True,
    )

    close_parser = subparsers.add_parser(
        CLOSE_ISSUE_PARSER,
        description=(
            "Close issues in student repos based on a regex. For each master "
            "repository specified, the student list is traversed. For every "
            "student repo found, any open issues matching the `--title-regex` "
            "are closed."
        ),
        help="Close issues in student repos.",
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    close_parser.add_argument(
        "-r",
        "--title-regex",
        help=(
            "Regex to match titles against. Any issue whose title matches the "
            "regex will be closed."
        ),
        type=str,
        required=True,
    )

    list_parser = subparsers.add_parser(
        LIST_ISSUES_PARSER,
        description="List issues in student repos.",
        help="List issues in student repos.",
        parents=base_parsers,
        formatter_class=_OrderedFormatter,
    )
    list_parser.add_argument(
        "-r",
        "--title-regex",
        help=(
            "Regex to match against titles. Only issues matching this regex "
            "will be listed."
        ),
    )
    list_parser.add_argument(
        "-b",
        "--show-body",
        action="store_true",
        help="Show the body of the issue, alongside the default info.",
    )
    list_parser.add_argument(
        "-a",
        "--author",
        help="Only show issues by this author (GitHub username).",
        type=str,
        default=None,
    )
    state = list_parser.add_mutually_exclusive_group()
    state.add_argument(
        "--open",
        help="List open issues (default).",
        action="store_const",
        dest="state",
        const=apimeta.IssueState.OPEN,
    )
    state.add_argument(
        "--closed",
        help="List closed issues.",
        action="store_const",
        dest="state",
        const=apimeta.IssueState.CLOSED,
    )
    state.add_argument(
        "--all",
        help="List all issues (open and closed).",
        action="store_const",
        dest="state",
        const=apimeta.IssueState.ALL,
    )
    list_parser.set_defaults(state=apimeta.IssueState.OPEN)


class _OrderedFormatter(argparse.HelpFormatter):
    """A formatter class for putting out the help section in a proper order.
    All of the arguments that are configurable in the configuration file
    should appear at the bottom (in arbitrary, but always the same, order).
    Any other arguments should appear in the order they are added.

    The internals of the formatter classes are technically not public,
    so this class is "unsafe" when it comes to new versions of Python. It may
    have to be disabled for future versions, but it works for 3.5, 3.6 and 3.7
    at the time of writing. If this turns troublesome, it may be time to
    switch to some other CLI library.
    """

    def add_arguments(self, actions):
        """Order actions by the name  of the long argument, and then add them
        as arguments.

        The order is the following:

        [ NON-CONFIGURABLE | CONFIGURABLE | DEBUG ]

        Non-configurable arguments added without modification, which by
        default is the order they are added to the parser. Configurable
        arguments are added in the order defined by
        :py:const:`config.ORDERED_CONFIGURABLE_ARGS`. Finally, debug commands
        (such as ``--traceback``) are added in arbitrary (but consistent)
        order.
        """
        args_order = tuple(
            "--" + name.replace("_", "-")
            for name in config.ORDERED_CONFIGURABLE_ARGS
        ) + ("--traceback",)

        def key(action):
            if len(action.option_strings) < 2:
                return -1
            long_arg = action.option_strings[1]
            if long_arg in args_order:
                return args_order.index(long_arg)
            return -1

        actions = sorted(actions, key=key)
        super().add_arguments(actions)


def _create_parser():
    """Create the parser."""

    parser = argparse.ArgumentParser(
        prog="repobee",
        description=(
            "A CLI tool for administering large amounts of git repositories "
            "on GitHub instances. See the full documentation at "
            "https://repobee.readthedocs.io"
        ),
        formatter_class=_OrderedFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        help="Display version info",
        action="version",
        version="{} v{}".format(repobee.__package__, repobee.__version__),
    )
    _add_subparsers(parser)
    return parser


def _add_subparsers(parser):
    """Add all of the subparsers to the parser. Note that the parsers prefixed
    with `base_` do not have any parent parsers, so any parser inheriting from
    them must also inherit from the required `base_parser` (unless it is a
    `base_` prefixed parser, of course).
    """

    base_parser, base_student_parser, base_user_parser, master_org_parser = (
        _create_base_parsers()
    )

    repo_name_parser = argparse.ArgumentParser(
        add_help=False, parents=[base_parser]
    )
    repo_name_parser.add_argument(
        "-mn",
        "--master-repo-names",
        help="One or more names of master repositories. Names must either "
        "refer to local directories, or to master repositories in the "
        "target organization.",
        type=str,
        required=True,
        nargs="+",
    )

    subparsers = parser.add_subparsers(dest=SUB)
    subparsers.required = True

    subparsers.add_parser(
        SHOW_CONFIG_PARSER,
        help="Show the configuration file",
        description=(
            "Show the contents of the configuration file. If no configuration "
            "file can be found, show the path where repobee expectes to find "
            "it."
        ),
        formatter_class=_OrderedFormatter,
    )

    subparsers.add_parser(
        SETUP_PARSER,
        help="Setup student repos.",
        description=(
            "Setup student repositories based on master repositories. "
            "This command performs three primary actions: sets up the "
            "student teams, creates one student repository for each "
            "master repository and finally pushes the master repo files to "
            "the corresponding student repos. It is perfectly safe to run "
            "this command several times, as any previously performed step "
            "will simply be skipped."
        ),
        parents=[
            base_user_parser,
            base_student_parser,
            master_org_parser,
            repo_name_parser,
        ],
        formatter_class=_OrderedFormatter,
    )

    update = subparsers.add_parser(
        UPDATE_PARSER,
        help="Update existing student repos.",
        description="Push changes from master repos to student repos.",
        parents=[
            base_user_parser,
            base_student_parser,
            master_org_parser,
            repo_name_parser,
        ],
        formatter_class=_OrderedFormatter,
    )
    update.add_argument(
        "-i",
        "--issue",
        help=(
            "Path to issue to open in repos to which update pushes fail. "
            "Assumes that the first line is the title."
        ),
        type=str,
    )

    subparsers.add_parser(
        MIGRATE_PARSER,
        help="Migrate repositories into the target organization.",
        description=(
            "Migrate repositories into the target organization. "
            "The repos must be local on disk to be migrated. Note that "
            "migrated repos will be private."
        ),
        parents=[repo_name_parser, base_user_parser],
        formatter_class=_OrderedFormatter,
    )

    clone = subparsers.add_parser(
        CLONE_PARSER,
        help="Clone student repos.",
        description="Clone student repos asynchronously in bulk.",
        parents=[base_student_parser, repo_name_parser],
        formatter_class=_OrderedFormatter,
    )

    plug.manager.hook.clone_parser_hook(clone_parser=clone)

    _add_issue_parsers([base_student_parser, repo_name_parser], subparsers)
    _add_peer_review_parsers(
        [base_student_parser, repo_name_parser], subparsers
    )

    subparsers.add_parser(
        VERIFY_PARSER,
        help="Verify your settings, such as the base url and the OAUTH token.",
        description=(
            "Verify core settings. Performs the following checks, in order: "
            "user exists (implicitly verifies base url), oauth scopes "
            "(premissions of "
            "the OAUTH token), organization exists, user "
            "is an owner of the "
            "organization (for both target org and "
            "master org if the latter is "
            "specified). If any one of "
            "the checks fails, the verification is "
            "aborted and an error "
            "message is displayed."
        ),
        parents=[base_parser, base_user_parser, master_org_parser],
        formatter_class=_OrderedFormatter,
    )


def _create_base_parsers():
    """Create the base parsers."""
    configured_defaults = config.get_configured_defaults()
    config.execute_config_hooks()

    default = (
        lambda arg_name: configured_defaults[arg_name]
        if arg_name in configured_defaults
        else None
    )
    is_required = (
        lambda arg_name: True if arg_name not in configured_defaults else False
    )

    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument(
        "-o",
        "--org-name",
        help="Name of the target organization",
        type=str,
        required=is_required("org_name"),
        default=default("org_name"),
    )
    base_parser.add_argument(
        "-g",
        "--github-base-url",
        help=(
            "Base url to a GitHub v3 API. For enterprise, this is usually "
            "`https://<HOST>/api/v3`"
        ),
        type=str,
        required=is_required("github_base_url"),
        default=default("github_base_url"),
    )
    base_parser.add_argument(
        "-t",
        "--token",
        help="OAUTH token for the GitHub instance. Can also be specified in "
        "the `REPOBEE_OAUTH` environment variable.",
        type=str,
        default=default("token"),
    )

    base_parser.add_argument(
        "-tb",
        "--traceback",
        help="Show the full traceback of critical exceptions.",
        action="store_true",
    )
    # base parser for when student lists are involved
    base_student_parser = argparse.ArgumentParser(add_help=False)
    students = base_student_parser.add_mutually_exclusive_group(
        required=is_required("students_file")
    )
    students.add_argument(
        "-sf",
        "--students-file",
        help="Path to a list of student usernames.",
        type=str,
        default=default("students_file"),
    )
    students.add_argument(
        "-s",
        "--students",
        help="One or more whitespace separated student usernames.",
        type=str,
        nargs="+",
    )

    # base parser for when files need to be pushed
    base_user_parser = argparse.ArgumentParser(add_help=False)

    # the username is required for any pushing
    base_user_parser.add_argument(
        "-u",
        "--user",
        help=(
            "Your GitHub username. Needed for pushing without CLI "
            "interaction."
        ),
        type=str,
        required=is_required("user"),
        default=default("user"),
    )

    master_org_parser = argparse.ArgumentParser(add_help=False)
    master_org_parser.add_argument(
        "-mo",
        "--master-org-name",
        help="Name of the organization containing the master repos. "
        "Defaults to the same value as `-o|--org-name` if left unspecified. "
        "Note that config values take precedence over this default.",
        default=default("master_org_name"),
    )

    return (
        base_parser,
        base_student_parser,
        base_user_parser,
        master_org_parser,
    )


@contextmanager
def _sys_exit_on_expected_error():
    try:
        yield
    except exception.PushFailedError as exc:
        LOGGER.error(
            "There was an error pushing to {}. "
            "Verify that your token has adequate access.".format(exc.url)
        )
        sys.exit(1)
    except exception.CloneFailedError as exc:
        LOGGER.error(
            "There was an error cloning from {}. "
            "Does the repo really exist?".format(exc.url)
        )
        sys.exit(1)
    except exception.GitError:
        LOGGER.error("Something went wrong with git. See the logs for info.")
        sys.exit(1)
    except exception.APIError as exc:
        LOGGER.error("Exiting beacuse of {.__class__.__name__}".format(exc))
        sys.exit(1)


def _extract_groups(args: argparse.Namespace) -> List[str]:
    """Extract groups from args namespace.`

    Args:
        args: A namespace object.

    Returns:
        a list of student usernames, or None of neither `students` or
        `students_file` is in the namespace.
    """
    if "students" in args and args.students:
        students = [apimeta.Team(members=[s]) for s in args.students]
    elif "students_file" in args and args.students_file:
        students_file = pathlib.Path(args.students_file)
        try:  # raises FileNotFoundError in 3.5 if no such file exists
            students_file = students_file.resolve()
        except FileNotFoundError:
            pass  # handled by next check
        if not students_file.is_file():
            raise exception.FileError(
                "'{!s}' is not a file".format(students_file)
            )
        if not students_file.stat().st_size:
            raise exception.FileError("'{!s}' is empty".format(students_file))
        students = [
            apimeta.Team(members=[s for s in group.strip().split()])
            for group in students_file.read_text(
                encoding=sys.getdefaultencoding()
            ).split(os.linesep)
            if group  # skip blank lines
        ]
    else:
        students = None

    return students


def _identify_api(base_url, token):
    ssl_verify = not os.getenv("REPOBEE_NO_VERIFY_SSL") == "true"
    if not ssl_verify:
        LOGGER.warning("SSL verification turned off, only for testing")
    gitlab_response = requests.get(
        "{}/api/v4/users?per_page=1".format(base_url),
        headers={"Private-Token": token},
        verify=ssl_verify,
    )
    if gitlab_response.status_code == 200:
        LOGGER.warning(
            "Using a GitLab API. GitLab support is in alpha and unstable."
        )
        return gitlab_api.GitLabAPI
    return github_api.GitHubAPI


def _connect_to_api(
    base_url: str, token: str, org_name: str, user: str
) -> github_api.GitHubAPI:
    """Return a GitHubAPI instance connected to the specified API endpoint."""
    try:
        api = _identify_api(base_url, token)(base_url, token, org_name, user)
    except exception.NotFoundError:
        # more informative message
        raise exception.NotFoundError(
            "either organization {} could not be found, "
            "or the base url '{}' is incorrect".format(org_name, base_url)
        )
    return api


def _repo_names_to_urls(
    repo_names: Iterable[str], org_name: str, api: github_api.GitHubAPI
) -> List[str]:
    """Use the repo_names to extract urls to the repos. Look for git
    repos with the correct names in the local directory and create local uris
    for them.  For the rest, create urls to the repos assuming they are in the
    target organization. Do note that there is _no_ guarantee that the remote
    repos exist as checking this takes too much time with the REST API.

    A possible improvement would be to use the GraphQL API for this function.

    Args:
        repo_names: names of repositories.
        org_name: Name of the organization these repos are expected in.
        api: A GitHubAPI instance.

    Returns:
        a list of urls corresponding to the repo_names.
    """
    local = [
        name for name in repo_names if util.is_git_repo(os.path.abspath(name))
    ]
    non_local = [name for name in repo_names if name not in local]

    non_local_urls = api.get_repo_urls(non_local, org_name)
    local_uris = [
        pathlib.Path(os.path.abspath(repo_name)).as_uri()
        for repo_name in local
    ]
    return non_local_urls + local_uris


def parse_plugins(sys_args: Tuple[str]):
    """Parse all plugin arguments.

    Args:
        sys_args: Command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog="repobee", description="plugin pre-parser for repobee."
    )

    mutex_grp = parser.add_mutually_exclusive_group(required=True)
    mutex_grp.add_argument(
        "-p",
        "--plug",
        help="Specify the name of a plugin to use.",
        type=str,
        action="append",
    )
    mutex_grp.add_argument(
        "--no-plugins", help="Disable plugins.", action="store_true"
    )

    args = parser.parse_args(sys_args)

    return args
