"""Module representing a city or settlement"""

from katan_ai.katan.board.building import Building
from katan_ai.katan.board.building_type import BuildingType
from katan_ai.katan.board.coords import Coords
from katan_ai.katan.player import Player


class IntersectionBuilding(Building):
    """A building that is built on a intersection. In the base game, a settlement or a city.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            coords (Coords): The coords the building is at

    Args:
            owner: The player who owns this building
            building_type: The type of building this is
            coords: The coords the building is at
    """

    def __init__(self, owner: Player, building_type: BuildingType, coords: Coords):
        super().__init__(owner, building_type)
        self.coords = coords
