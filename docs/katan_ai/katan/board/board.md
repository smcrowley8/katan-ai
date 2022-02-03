Module katan_ai.katan.board.board
=================================
Module representing a basic catan board

Classes
-------

`Board(hexes: Set[Hex], harbors: Set[Harbor] = set(), robber: Coords = None)`
:   An interface for holding the state of Catan boards.

    Uses a triangular grid to hold the tiles, intersections and
    paths. The Board constructor will automatically
    generate the intersections and paths from a dict of hexes,
    assuming all the hexes tile correctly.

    Args:
        hexes:
            The hexes on the board, keyed by their coordinates
        harbors:
            The harbors on the board
        robber:
            The initial coordinates of the robber. If None, then will automatically place the robber on the first
            desert hex it can find, and raise an error if there are non

    Attributes:
        hexes (Dict[Coord, Hex]):
            The hexes on this catan board, keyed by their coordinates
        intersections: (Dict[Coords, Intersection]):
            The intersections on the board, keyed by their coordinates
        paths (Dict[frozenset[Coords], Path]):
            The paths on the board, keyed by the coordinates of the two intersections they connect
        harbors (Dict[frozenset[Coords], Harbor]):
            The harbors on the board, keyed by the coords of the path they are attached to
        robber (Set[Coords]): The location of the robber

    ### Descendants

    * katan_ai.katan.board.beginner_board.BeginnerBoard
    * katan_ai.katan.board.random_board.RandomBoard

    ### Methods

    `add_intersection_building(self, player: Player, coords: Coords, building_type: BuildingType, ensure_connected: Optional[bool] = True)`
    :   Add an intersection building to the board.

        Args:
            player: The player who owns the settlement
            coords: The coords to put the building
            ensure_connected: Whether to ensure that the building is connected to the player's roads. Defaults to True
        Raises:
            InvalidCoordsError: If coords is not a valid intersection
            TooCloseToBuildingError: If the building is too close to another building
            PositionAlreadyTakenError: If the position is already taken

    `add_path_building(self, player: Player, building_type: BuildingType, path_coords: Set[Coords], ensure_connected: Optional[bool] = True)`
    :   Add an path building to the board.

        Do not check if the player has enough resources, or any other checks other than the building's location being valid.

        Args:
            player: The player adding the building
            building_type: The building_type of the building being added
            path_coords: The coordinates the path to build the building on (i.e. the coordinates of the two intersections the path connects)
            ensure_connected: Whether to ensure that the path building is connected to another building. Defaults to True
        Raises:
            ValueError: If the path_coords are not valid
            CoordsBlockedError: If there is already a building on the path
            NotConnectedError: If check_connection is true and the building is not connected to anything

    `assert_valid_city_coords(self, player: Player, coords: Coords)`
    :   Check whether the coordinates given are a valid place to build a city by the player given.

        Args:
            player: The player building the city
            coords: Where to build the city

    `assert_valid_road_coords(self, player: Player, path_coords: Set[Coords], ensure_connected: Optional[bool] = True)`
    :   Assert that a given edge is a valid place for the player to build a road.

        Args:
            player: The player
            path_coords: The coordinates of the two intersections connected by the path
            ensure_connected: Whether to assert that the path is connected to the player's existing roads or settlements

    `assert_valid_settlement_coords(self, coords: Coords, player: Player, ensure_connected: Optional[bool]) ‑> None`
    :   Check whether the coordinates given are a valid place to build a settlement.

        Does not return anything, but raises an error if the coordinates are not valid.

        Args:
            coords: The coordinates to check
            player: The player building the settlement
            ensure_connected: Whether the check if the settlement will be connected by road
        Raises:
            TooCloseToBuildingError: If the building is too close to another building
            PositionAlreadyTakenError: If the position is already taken
            NotConnectedError: If `check_connection` is `True` and the settlement is not connected

    `calculate_player_longest_road(self, player: Player) ‑> int`
    :   Calculate the length of the longest road segment for the player given.

        Args:
            player: The player to calculate the longest road for
        Returns:
            The length of the ongest road segment

    `get_connected_hex_intersections(self, hex: Hex) ‑> Set[katan_ai.katan.board.intersection.Intersection]`
    :   Get all of the intersections that are connected to the hex.

        Args:
            hex: The hex

        Returns:
            All 6 intersections that are around this hex

    `get_hex_resources_for_intersection(self, coords: Coords) ‑> Dict[katan_ai.katan.resource.Resource, int]`
    :   Get the associated resources for the hexes around the intersection at the coords given.

        Args:
            coords: The coordinates of an intersection
        Returns:
            The amounts of resources from the hexes around this intersection

    `get_hexes_connected_to_intersection(self, intersection_coords: Coords) ‑> Set[katan_ai.katan.board.coords.Coords]`
    :   Get all the hexes' coordinates that are connected to the intersection with the coordinates provided.

        Args:
            intersection_coords: The coords of an intersection
        Returns:
            The hexes connected to the intersection

    `get_intersection_connected_intersections(self, intersection: Intersection) ‑> Set[katan_ai.katan.board.intersection.Intersection]`
    :   Get all the intersections connected to the intersection given by an path.

        Args:
            intersection: The intersection to get the connected intersections for

        Returns:
            The intersections that are connected to the intersection given

    `get_paths_for_intersection_coords(self, coords: Coords) ‑> Set[katan_ai.katan.board.path.Path]`
    :   Get all the paths who that connected to the intersection given.

        Args:
            coords: The coordinates of the intersection
        Returns:
            A set of the paths attached to that intersection

    `get_players_on_hex(self, coords: Coords) ‑> Set[katan_ai.katan.player.Player]`
    :   Get all the players who have a building on the edge of the given hex.

        Args:
            coords: The coords of the hex
        Returns:
            The players with a building on the edge of the hex

    `get_valid_city_coords(self, player: Player) ‑> Set[katan_ai.katan.board.coords.Coords]`
    :   Get all the valid city coordinates for the player to build a city.

        Args:
            player (Player): The player building the city
        Returns
            The coordinates of all the valid city locations

    `get_valid_road_coords(self, player: Player, ensure_connected: Optional[bool] = True, connected_intersection: Optional[Coords] = None) ‑> Set[FrozenSet[katan_ai.katan.board.coords.Coords]]`
    :   Get all the valid coordinates for the player to build a road.

        Args:
            player: The player building the road
            ensure_connected:
                Whether to only return the path coordinates that are connected to the player's existing roads/settlements. Defaults to True
            connected_intersection: The coords of an intersection that the potential road must be attached to. Defaults to None
        Returns:
            The coordinates of all the paths where the player can build a road.

    `get_valid_settlement_coords(self, player: Player, ensure_connected: Optional[bool] = True) ‑> Set[katan_ai.katan.board.coords.Coords]`
    :   Get all the valid settlement coordinates for the player to build a settlement.

        Args:
            player: The player to check for valid settlement coordinates
            ensure_connected: Whether to ensure the coordinates are connected to the player's roads
        Returns:
            The coordinates of all the valid settlement intersections

    `get_yield_for_roll(self, roll: int) ‑> Dict[katan_ai.katan.player.Player, katan_ai.katan.roll_yield.RollYield]`
    :   Calculate the resources given out for a particular roll.

        Args:
            roll: The number rolled
        Returns:
            The RollYield object containing the information for what each player gets, keyed by the player

    `is_valid_city_coords(self, player: Player, coords: Coords) ‑> bool`
    :   Check whether the coordinates given are valid city coordinates.

        Args:
            player: The player
            coords: The coordinates to check
        Returns:
            Whether the coords are a valid place for the player to build a city

    `is_valid_hex_coords(self, coords: Coords) ‑> bool`
    :   Check whether the coordinates given are valid hex coordinates.

        Args:
            coords: The coordinates
        Returns:
            Whether there is a hex at those coordinates

    `is_valid_road_coords(self, player: Player, path_coords: Set[Coords], ensure_connected: Optional[bool] = True) ‑> bool`
    :   Check whether the path coordinates given are valid road coordinate for the player given.

        Args:
            player: The player
            path_coords: The coordinates of the path
            ensure_connected: Whether to ensure that the road is connected to the player's existing roads/buildings. Defaults to True
        Returns:
            Whether the player can build a road on this path

    `is_valid_settlement_coords(self, player: Player, coords: Coords, ensure_connected: Optional[bool]) ‑> bool`
    :   Check whether the given coordinates are a valid place for the player to build a settlement.

        Args:
            player: The player
            coords: The coordinates to check
            ensure_connected: Whether to ensure that the settlement will be connected to the player's roads
        Returns:
            Whether the coordinates are a valid settlement location for the player
