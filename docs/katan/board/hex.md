Module katan_ai.katan.board.hex
===============================
Module representing a catan hex (board space)

Classes
-------

`Hex(coords: katan_ai.katan.board.coords.Coords, hex_type: katan_ai.katan.board.hex_type.HexType, token_number: Optional[int] = None)`
:   A hex on a Catan board.

    Args:
        coords: The coordinates of this hex
        hex_type: The type of this hex
        token_number: The number of the token on this hex, or None if the hex is a desert

    Attributes:
        CONNECTED_POINTS_OFFSETS (Set[Coords]):
                The offsets of the connected points from a hex's coordinates
        coords (Coords): The coordinates of this hex
        hex_type (HexType): The type of this hex
        token_number (int): The number of the token on this hex

    ### Class variables

    `CONNECTED_CORNER_OFFSETS: Set[katan_ai.katan.board.coords.Coords]`
    :
