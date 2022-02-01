"""Main cli entry point"""
from re import L
import sys

import click
from rich.console import Console  # , ConsoleThreadLocals

from .commands.colonistCommands import command_join_lobby


@click.group()
def cli() -> None:
    """Main entrypoint for cli"""

    console = Console()
    console.log("Entering KatanAI CLI...")


@cli.command()
@click.option(
    "--lobbyID", "-LID", type=click.types.STRING, help="ID for the game lobby to join"
)
def join_lobby(lobbyID: str) -> None:
    """Join a colonist.io game given the game lobby"""
    command_join_lobby(lobbyID=lobbyID)
