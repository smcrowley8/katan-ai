from __future__ import annotations


class Coords:
    """
    A class used to represent coordinates on the Catan board.

    Stores a coordinate on a triangular grid, so that each
    hex and point both has a unique coord.

    Args:
            q (int): The q coordinate
            r (int): The r coordinate
    """

    def __init__(self, q: int, r: int) -> None:
        self.q = q
        self.r = r

    def __hash__(self) -> int:
        return hash((self.q, self.r))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coords):
            # TODO
            return False
        return self.q == other.q and self.r == other.r

    def __add__(self, other: Coords) -> Coords:
        return Coords(self.q + other.q, self.r + other.r)

    def __sub__(self, other: Coords) -> Coords:
        return Coords(self.q - other.q, self.r - other.r)

    def __str__(self) -> str:
        return "(q: %d, r:%d)" % (self.q, self.r)

    def __repr__(self) -> str:
        return self.__str__()
