Module katan_ai.katan.board.path
================================
Module representing a path from one coord to another

Classes
-------

`Path(path_coords: Set[katan_ai.katan.board.coords.Coords], building: Optional[katan_ai.katan.board.building.PathBuilding] = None)`
:   A path on a Catan board.

    Args:
            path_coords: The coordinates of the two intersections
                that the path connects.
            building: The building on this path.
    Attributes:
            path_coords (set(Coords, Coords)): The coordinates of the two intersections
                that the path connects.
            building (PathBuilding, optional): The building on this path.

    ### Methods

    `other_intersection(self, coords: katan_ai.katan.board.coords.Coords) ‑> katan_ai.katan.board.coords.Coords`
    :   Given one of the intersection coords for this path, returns the other one.

        Args:
            coords: The intersection coords
