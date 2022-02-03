Module katan_ai.katan.board.building_type
=========================================
Module representing the type of catan building

Classes
-------

`BuildingType(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   A type of building in a Catan game.

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `CITY`
    :   The cities

    `ROAD`
    :   The roads

    `SETTLEMENT`
    :   The settlements

    ### Methods

    `get_required_resources(self)`
    :   Get the resources required to build this building.

        Returns:
            Dict[Resource, int]: The amount of each resource required to build this building
