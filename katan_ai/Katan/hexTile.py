"""Representative of a hexTile"""
from __future__ import annotations

from typing import List


class Vertex:
    """Each hex tile has 6 vertices
    each vertex connects to 2 or 3 other vertices
    each vertex has 6 possible connectors, only 3 are ever not Null"""

    def __init__(self, orientation: bool, owners: List[HexTile]) -> None:
        """initializes a vertex with a reference to owners"""
        self.up_right_node = None
        self.up_left_node = None
        self.up_node = None
        self.down_right_node = None
        self.down_left_node = None
        self.down_node = None


class HexTile:
    """Represents a tile on the katan game board"""

    def __init__(self) -> None:
        pass
