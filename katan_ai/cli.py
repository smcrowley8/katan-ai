"""CLI entry point"""
# from re import L
# import sys
from typing import Optional

import click
from rich.console import Console  # , ConsoleThreadLocals

from katan_ai.commands.colonistCommands import command_join_lobby
from katan_ai.commands.gameCommands import command_make_game
from katan_ai.katan.game import Game

GAME: Optional[Game] = None


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
    global GAME
    command_join_lobby(lobbyID=lobbyID)
    # TODO: get board setup and player order from the site
    # TODO: have game creation be based off board data gotten from above
    GAME = command_make_game()


if __name__ == "__main__":
    """Run main cli"""
    cli()
