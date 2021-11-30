from logging import getLogger

import os
import sys

import click
import uvicorn

logger = getLogger(__name__)


@click.group()
def cli(**cli_kwargs):
    # do something
    return


@cli.command("runserver")
@click.option(
    "-H",
    "--host",
    default="127.0.0.1",
    help="Bind socket to this host.  [default: 127.0.0.1]",
)
@click.option(
    "-P", "--port", default=8000, help="Bind socket to this port.  [default: 8000]"
)
def runserver(**cli_kwargs):
    kwargs = {
        "app": "ddns_clienter.asgi:application",
        # "host": host,
        # "port": port,
        "lifespan": "off",
        "log_level": "info",
        "access_log": False,
    }
    kwargs.update(cli_kwargs)

    return uvicorn.run(**kwargs)


@cli.command("check_and_push")
@click.option("-C", "--config", required=True, type=str, help="config.toml")
def check_and_push(**cli_kwargs):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ddns_clienter.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def main():
    cli()
