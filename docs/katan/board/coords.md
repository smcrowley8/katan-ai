Module katan_ai.katan.board.coords
==================================
Module for representing coordinates used to identify roads, buildings, and hexes in the catan game

Classes
-------

`Coords(q, r)`
:   A class used to represent coordinates on the Catan board.

    Stores a coordinate on a triangular grid, so that each
    hex and point both has a unique coord.

    Args:
            q (int): The q coordinate
            r (int): The r coordinate
