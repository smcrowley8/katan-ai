Module katan_ai.katan.board.intersection_building
=================================================
Module representing a city or settlement

Classes
-------

`IntersectionBuilding(owner: katan_ai.katan.player.Player, building_type: katan_ai.katan.board.building_type.BuildingType, coords: katan_ai.katan.board.coords.Coords)`
:   A building that is built on a intersection. In the base game, a settlement or a city.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            coords (Coords): The coords the building is at

    Args:
            owner: The player who owns this building
            building_type: The type of building this is
            coords: The coords the building is at

    ### Ancestors (in MRO)

    * katan_ai.katan.board.building.Building
