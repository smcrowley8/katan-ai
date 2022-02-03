Module katan_ai.katan.roll_yield
================================
Contains representation for where a rolls yield comes from and what it is

Classes
-------

`RollYield()`
:   A utility class to represent what each player gets from a roll of the dice.

    Contains information about where the resources came from as well.

    Attributes:
            total_yield (Dict[Resource, int]): The total yield from this dice roll
            all_yields (Set[RollYieldSource]): The sources where the resources came from

    ### Methods

    `add_yield(self, resource: katan_ai.katan.resource.Resource, amount: int, source: katan_ai.katan.roll_yield.RollYieldSource) ‑> None`
    :   Add a yield to the RollYield.

        Also updates total_yield. Use this method instead of directly changing all_yields.

        Args:
            resource: The resource the player has received
            amount: The amount of the resource the player has received

`RollYieldSource(resource: katan_ai.katan.resource.Resource, amount: int, building: katan_ai.katan.board.intersection_building.IntersectionBuilding, hex: katan_ai.katan.board.hex.Hex)`
:   The source of some resources a player got after rolling the dice.

    Attributes:
        resource: The resource earned,
        amount: The amount of the resource earned
        building: The building that earned the resources
        hex: The hex that the resources came from
