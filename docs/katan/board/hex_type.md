Module katan_ai.katan.board.hex_type
====================================
Module representing the resource afiiliated with a hex

Classes
-------

`HexType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   The different types of hexes in the game.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `DESERT`
    :   The desert hex type

    `FIELDS`
    :   The fields hex type

    `FOREST`
    :   The forest hex type

    `HILLS`
    :   The hills hex type

    `MOUNTAINS`
    :   The mountains hex type

    `PASTURE`
    :   The pasture hex type

    ### Methods

    `get_resource(self) ‑> katan_ai.katan.resource.Resource`
    :   Get the resource the player receives when a hex of this type is activated.

        Returns:
            Resource: The resource the player would get
            None: If the player would not get a resource (i.e. a desert hex)
