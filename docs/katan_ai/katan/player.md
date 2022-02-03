Module katan_ai.katan.player
============================
Represents a player in a katan game

Classes
-------

`Player()`
:   A Player in a Catan game.

    Attributes:
            resources (Dict[Resource, int]): How many of each resource this player has
            development_cards (Dict[DevelopmentCard, int]): How many of each development card this player has
            connected_harbors (Set[Harbor]): The harbors this player is connected to. Used to determine the valid trades

    Creates dict for resources this player has available.
    Creates dicts for development cards this player has available.
    Creates a set for any harbors the player is connected to.
    Creates a counter for how many knights have been played.

    ### Methods

    `add_resources(self, resources: Dict[katan_ai.katan.resource.Resource, int]) ‑> None`
    :   Add some resources to this player's hand.

        Args:
            resources: Dict[Resource, int]: The resources to add to this players hand.

    `get_possible_trades(self) ‑> List[Dict[katan_ai.katan.resource.Resource, int]]`
    :   Get a list of the possible trades for this player.

        Returns: List[Dict[Resource, int]]
            The possible trades for this player.
            Negative numbers mean the player would give away those resources, positive numbers mean the player would receive those resources

    `get_random_resource(self) ‑> Optional[katan_ai.katan.resource.Resource]`
    :   Get a random resource from this player.

        Weighs the different resources depending on how many the player has.
        This is equavalent to randomly picking a resource out of the player's hand, i.e. when stealing a card via a knight card or rolling a 7.

        Returns:
            The resource, or None if the player has no resources

    `has_resources(self, resources: Dict[katan_ai.katan.resource.Resource, int]) ‑> bool`
    :   Check if the player has the resources needed to make the purchase given.

        Args:
            resources: Dict[Resource, int]: The resources to check that the player has

        Returns:
            bool: True if the player has the resources, false otherwise

    `play_development_card(self, card: katan_ai.katan.development_card.DevelopmentCard) ‑> None`
    :   Mark a development card as played and remove form players hand.

        Args:
            card: The card to play
        Raises:
            ValueError: If the player does not have the card

    `remove_resources(self, resources: Dict[katan_ai.katan.resource.Resource, int]) ‑> None`
    :   Remove the given resources from the player's hand.

        Args:
            resources: Dict[Resource, int]: The resources to remove.

        Raises:
            NotEnoughResourcesError: If the player does not have the resources.
