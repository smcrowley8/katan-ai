Module katan_ai.katan.board.intersection
========================================
Module representing the intersections where paths meet

Classes
-------

`Intersection(coords: katan_ai.katan.board.coords.Coords, building: Optional[katan_ai.katan.board.intersection_building.IntersectionBuilding] = None)`
:   A intersection on the Catan board.

    Args:
        coords:
                The coordinates of the intersection.
        building:
                The building on the intersection.

    Attributes:
            CONNECTED_CORNER_OFFSETS (Set[Coords]):
                    The offsets of the intersections that are connected by an path.
                    i.e. to get the connected intersections, add a intersection's coords to these values,
                    and then filter for which coords are valid intersection coords.
            coords (Coords):
                    The coordinates of the intersection.
            building (IntersectionBuilding, optional):
                    The building on the intersection.

    ### Class variables

    `CONNECTED_CORNER_OFFSETS: Set[katan_ai.katan.board.coords.Coords]`
    :
