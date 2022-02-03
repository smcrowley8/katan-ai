Module katan_ai.katan.board.board_renderer
==========================================
Module for rendering board on a terminal

Classes
-------

`BoardRenderer(board: Board, player_color_map: Optional[Dict[Player, str]] = {}, hex_color_map: Optional[Dict[HexType, str]] = {<HexType.FIELDS: 3>: '#ffea29', <HexType.FOREST: 0>: '#005e09', <HexType.PASTURE: 2>: '#52ff62', <HexType.HILLS: 1>: '#cc1f0c', <HexType.MOUNTAINS: 4>: '#7a7a7a', <HexType.DESERT: 5>: '#ffe5a3'}, resource_color_map: Optional[Dict[Resource, str]] = {<Resource.GRAIN: 3>: '#ffea29', <Resource.LUMBER: 0>: '#005e09', <Resource.WOOL: 2>: '#52ff62', <Resource.BRICK: 1>: '#cc1f0c', <Resource.ORE: 4>: '#7a7a7a'})`
:   Class for rendering a board in the terminal and configuring its appearance.

    Args:
        board: The board to render
        player_color_map:
            A map of which colors to use for which players. Colors are string hex codes (i.e. '#FF0000')
        hex_color_map:
            A map of which colors to use for the different types of hexes. Colors are string hex codes (i.e. '#FF00000')
        resource_color_map:
            A map of which colors to use for the different resource harbors. Colors are string hex codes (i.e. '#FF00000')

    ### Class variables

    `DEFAULT_HEX_COLORS`
    :

    `DEFAULT_PLAYER_COLORS`
    :

    `DEFAULT_RESOURCE_COLORS`
    :

    `WATER_COLOR`
    :

    ### Methods

    `get_board_as_string(self, hex_labels: Optional[Dict[Hex, str]] = {}, intersection_labels: Optional[Dict[Intersection, str]] = {}, path_labels: Optional[Dict[Path, str]] = {}) ‑> str`
    :   Get the board as a large, multiline string that includes colors.

        Args:
            hex_labels: A dictionary of labels to put on the hexes instead of the numbered tokens
            intersection_labels: A dictionary of labels to put on the points
            path_labels: A dictionary of labels to put on the paths

        Returns:
            str: The board as a string

    `get_coords_as_xy(self, coords: Coords) ‑> Tuple[]`
    :   Get the coordinates given as x, y position.

        Args:
            coords: The coordinates
        Returns:
            The (x, y) position

    `render_board(self, hex_labels: Optional[Dict[Hex, str]] = {}, intersection_labels: Optional[Dict[Intersection, str]] = {}, path_labels: Optional[Dict[Path, str]] = {})`
    :   Render the board into the terminal.

        Args:
            hex_labels: A dictionary of labels to put on the hexes instead of the numbered tokens
            intersection_labels: A dictionary of labels to put on the points
            path_labels: A dictionary of labels to put on the paths
