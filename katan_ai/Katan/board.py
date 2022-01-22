"""Representation for a katan board"""

from typing import List

from .templates import BASIC_BOARD_SETUP


class Board:
    """represents a board in katan
    2D array is used to represent a board
        Even numbered rows are offset 0.5 to the left
        Odd numbered rows are offset 0.5 to the right

    Example Board setup


    """

    def __init__(
        self,
        boardSetup: List[List[int]] = BASIC_BOARD_SETUP,
    ) -> None:
        self.hexTileDict = {}
        self.board = boardSetup
