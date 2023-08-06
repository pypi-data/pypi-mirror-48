"""Main entrypoint for the repobee CLI application.

.. module:: main
    :synopsis: Main entrypoint for the repobee CLI application.

.. moduleauthor:: Simon Larsén
"""

import sys
from typing import List

import daiquiri

from repobee import cli
from repobee import plugin
from repobee import exception

LOGGER = daiquiri.getLogger(__file__)

_PRE_INIT_ERROR_MESSAGE = """exception was raised before pre-initialization was
complete. This is usually due to incorrect settings.
Try running the `verify-settings` command and see if
the problem can be resolved. If all fails, please open
an issue at https://github.com/repobee/repobee/issues/new
and supply the stack trace below.""".replace(
    "\n", " "
)


def _separate_args(args: List[str]) -> (List[str], List[str]):
    """Separate args into plugin args and repobee args."""
    plugin_args = []
    if args and (args[0].startswith("-p") or "plug" in args[0]):
        cur = 0
        while cur < len(args) and args[cur].startswith("-"):
            if args[cur].startswith("-p"):
                plugin_args += args[cur : cur + 2]
                cur += 2
            elif args[cur] == "--no-plugins":
                plugin_args.append(args[cur])
                cur += 1
            else:
                break
    return plugin_args, args[len(plugin_args) :]


def main(sys_args: List[str]):
    """Start the repobee CLI."""
    args = sys_args[1:]  # drop the name of the program
    traceback = False
    pre_init = True
    try:
        plugin_args, app_args = _separate_args(args)

        if plugin_args:
            parsed_plugin_args = cli.parse_plugins(plugin_args)
            if parsed_plugin_args.no_plugins:
                LOGGER.info("plugins disabled")
            else:
                plugin.initialize_plugins(parsed_plugin_args.plug)
        else:
            plugin.initialize_plugins()
        parsed_args, api = cli.parse_args(app_args)
        traceback = parsed_args.traceback
        pre_init = False
        cli.dispatch_command(parsed_args, api)
    except Exception as exc:
        # FileErrors can occur during pre-init because of reading the config
        # and we don't want tracebacks for those (afaik at this time)
        if traceback or (
            pre_init and not isinstance(exc, exception.FileError)
        ):
            LOGGER.error(str(exc))
            if pre_init:
                LOGGER.info(_PRE_INIT_ERROR_MESSAGE)
            LOGGER.exception("critical exception")
        else:
            LOGGER.error("{.__class__.__name__}: {}".format(exc, str(exc)))


if __name__ == "__main__":
    main(sys.argv)
