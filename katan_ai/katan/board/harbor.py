"""Module representing harbor trading ports for catan"""
from typing import Set

from katan_ai.katan.board.coords import Coords
from katan_ai.katan.resource import Resource


class Harbor:
    """A harbor on the catan board.

    Attributes:
        path_coords (Set[Coords]): The coordinates of the path that the harbor is attached to
        resource (Resource): The resource that the player can trade in 2-1
    Args:
        path_coords (Set[Coords]): The coordinates of the path that the harbor is attached to
        resource (Resource): The resource that the player can trade in 2-1
    """

    def __init__(self, path_coords: Set[Coords], resource: Resource):
        self.path_coords = path_coords
        self.resource = resource
