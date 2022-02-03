Module katan_ai.katan.board.building
====================================
Module representing a base building model as well as a road(PathBuilding)

Classes
-------

`Building(owner: katan_ai.katan.player.Player, building_type: katan_ai.katan.board.building_type.BuildingType)`
:   A building on the Catan board.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is

    Args:
            owner: The player who owns this building
            building_type: The type of building this is

    ### Descendants

    * katan_ai.katan.board.building.PathBuilding
    * katan_ai.katan.board.intersection_building.IntersectionBuilding

`PathBuilding(owner: katan_ai.katan.player.Player, building_type: katan_ai.katan.board.building_type.BuildingType, path_coords: Set[katan_ai.katan.board.coords.Coords])`
:   A building that is built on a path. In the base game, only roads.

    Attributes:
            owner (Player): The player who owns this building
            building_type (BuildingType): The type of building this is
            path_coords (Set[Coords]): The coordinates of the two intersections the building is connecting

    Args:
            owner: The player who owns this building
            building_type: The type of building this is
            path_coords: The coordinates of the two intersections the building is connecting

    ### Ancestors (in MRO)

    * katan_ai.katan.board.building.Building
