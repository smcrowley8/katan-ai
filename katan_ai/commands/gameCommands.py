"""Handles commands surrounding doing more abstract things with the katan game module"""
from ..katan import Game
from ..katan.board import RandomBoard


def command_make_game() -> Game:
    # TODO: add parameters for game creation to be based of the board and player order given
    return Game(RandomBoard())
