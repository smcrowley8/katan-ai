Module katan_ai.katan.errors
============================
Different types of errors that are raised when invalid input to provided.

Classes
-------

`CoordsBlockedError(*args, **kwargs)`
:   Error for when the coordinates are blocked already.

    ### Ancestors (in MRO)

    * katan_ai.katan.errors.InvalidCoordsError
    * builtins.Exception
    * builtins.BaseException

`InvalidCoordsError(*args, **kwargs)`
:   Generic error for when the coordinates passed are invalid for some reason.

    Parent class of other errors

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

    ### Descendants

    * katan_ai.katan.errors.CoordsBlockedError
    * katan_ai.katan.errors.NotConnectedError
    * katan_ai.katan.errors.RequiresSettlementError
    * katan_ai.katan.errors.TooCloseToBuildingError

`NotConnectedError(*args, **kwargs)`
:   Error for when the player is trying to build a settlement that is not connected by road.

    ### Ancestors (in MRO)

    * katan_ai.katan.errors.InvalidCoordsError
    * builtins.Exception
    * builtins.BaseException

`NotEnoughResourcesError(*args, **kwargs)`
:   Error when the player doesn't have enough resources to do this action.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`RequiresSettlementError(*args, **kwargs)`
:   Error for when trying to build a city that is not on top of an existing settlement.

    ### Ancestors (in MRO)

    * katan_ai.katan.errors.InvalidCoordsError
    * builtins.Exception
    * builtins.BaseException

`TooCloseToBuildingError(*args, **kwargs)`
:   Error for when a building is to close to the one the player is trying to build.

    ### Ancestors (in MRO)

    * katan_ai.katan.errors.InvalidCoordsError
    * builtins.Exception
    * builtins.BaseException
