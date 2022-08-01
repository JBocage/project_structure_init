"""This file implements a command line interface for launching generators"""

import pathlib

import click

from .. import __VERSION__


class Config(object):
    """An object designed to conatin and pass the config"""

    def __init__(self) -> None:
        self.config = {}

    def set_config(self, key, value):
        """Sets a key-value pair into the config"""
        self.config[key] = value


@click.group()
@click.version_option(version=__VERSION__)
@click.pass_context
def cli(ctx, *args, **kwargs):
    """Loads all high level kwargs into the config"""
    ctx.obj = Config()
    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)
        print(key, type(value), value)


@cli.command("init")
@click.option(
    "-v",
    "verbose",
    is_flag=True,
    help="Sets verbosity",
)
@click.argument("root_dir", type=click.Path(), required=False)
@click.pass_context
def init(ctx, *args, **kwargs):
    """initialise the makedoc profile for the directory"""

    for key, value in kwargs.items():
        ctx.obj.set_config(key, value)

    args = ctx.obj.config

    if args.pop("verbose"):
        print("Generating a doc file")

    root_dir_str = args.pop("root_dir")
    if root_dir_str is None:
        root_dir_str = "."
    pth = pathlib.Path(root_dir_str).resolve().absolute()
    print(pth)
