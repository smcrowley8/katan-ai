from typing import Set

from ..player import Player
from .building_type import BuildingType
from .coords import Coords


class Building:
    """A building on the Catan board.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is

    Args:
            owner: The player who owns this building
            building_type: The type of building this is
    """

    def __init__(self, owner: Player, building_type: BuildingType):
        self.owner = owner
        self.building_type = building_type


class PathBuilding(Building):
    """A building that is built on a path. In the base game, only roads.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            path_coords (Set[Coords]): The coordinates of the two intersections the building is connecting

    Args:
            owner: The player who owns this building
            building_type: The type of building this is
            path_coords: The coordinates of the two intersections the building is connecting
    """

    def __init__(
        self, owner: Player, building_type: BuildingType, path_coords: Set[Coords]
    ):
        super().__init__(owner, building_type)
        self.path_coords = path_coords
