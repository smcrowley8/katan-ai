Module katan_ai.katan.development_card
======================================
Module representing a development card

Classes
-------

`DevelopmentCard(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   A development card in a game of Catan.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `KNIGHT`
    :   The knight card

    `MONOPOLY`
    :   The monopoly card

    `ROAD_BUILDING`
    :   The road building card

    `VICTORY_POINT`
    :   Generic type to represent the victory point cards (i.e. library)

    `YEAR_OF_PLENTY`
    :   The year of plenty card

    ### Static methods

    `get_required_resources() ‑> Dict[katan_ai.katan.resource.Resource, int]`
    :   Get the resources required to build a development card.

        Returns:
            How many of each resource is required to build a development card
