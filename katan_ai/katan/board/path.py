"""Module representing a path from one coord to another"""
from typing import Optional, Set

from katan_ai.katan.board.building import PathBuilding
from katan_ai.katan.board.coords import Coords


class Path:
    """A path on a Catan board.

    Args:
            path_coords: The coordinates of the two intersections
                that the path connects.
            building: The building on this path.
    Attributes:
            path_coords (set(Coords, Coords)): The coordinates of the two intersections
                that the path connects.
            building (PathBuilding, optional): The building on this path.
    """

    def __init__(
        self, path_coords: Set[Coords], building: Optional[PathBuilding] = None
    ):
        self.path_coords = path_coords
        self.building = building

    def other_intersection(self, coords: Coords) -> Coords:
        """Given one of the intersection coords for this path, returns the other one.

        Args:
            coords: The intersection coords
        """
        return [c for c in self.path_coords if c != coords][0]
