Module katan_ai.katan.game
==========================

Classes
-------

`Game(board: katan_ai.katan.board.board.Board, num_players: Optional[int] = 4)`
:   A game of Catan. Holds all the game state and game logic for interacting with the board, players and decks.

    Args:
            board: The board to use in the Catan game
            num_players: The number of players to start the game with. Defaults to 4

    Attributes:
            board (Board): The Catan board being used in this game
            players (List[Player]): The players in the game, ordered by (recommended) turn order
            longest_road_owner (Player): The player who has the longest road token, or None if no players
                have a road of at least 5 length
            largest_army_owner (Player): The player how has the largest army, or None if no players have played at least 3 knight cards
            development_card_deck (List[DevelopmentCard]): The deck of development cards

    Initialize game based off of a given board setup and number of players

    ### Methods

    `add_yield(self, roll_yield: Dict[katan_ai.katan.player.Player, katan_ai.katan.roll_yield.RollYield])`
    :   Add the yield provided to the player's hands.

        Args:
            roll_yield: The yield provided by Board.get_yield_for_roll. A dictionary of RollYields mapped by
                the player who gets that yield

    `add_yield_for_roll(self, roll: int)`
    :   Add the resources to the player's hands for the dice roll given.

        Args:
            roll: The number that was rolled

    `build_development_card(self, player: katan_ai.katan.player.Player) ‑> katan_ai.katan.development_card.DevelopmentCard`
    :   Build a development card and place it in the player's hand.

        Args:
            player: The player building the development card
        Raises:
            NotEnoughResourcesError: If the player cannot afford to build a development card
        Returns:
            The card that the player built and has been added to their hand

    `build_road(self, player: katan_ai.katan.player.Player, path_coords: Set[katan_ai.katan.board.coords.Coords], cost_resources: Optional[bool] = True, ensure_connected: Optional[bool] = True)`
    :   Build a road.

        Args:
            player: The player who is building the road
            path_coords: The coordinates of the path to build a road on.
                Should be two valid connected intersection coordinates (i.e. {(1, 0), (1, -1)})
            cost_resources: Whether to remove resources from the player's hand to build the road,
                and raise an error if they don't have enough
            ensure_connected: Whether to ensure that the road is connected to another road, settlement or city
        Raises:
            NotEnoughResourcesError: If check_resources is True and the player doesn't have the cards to build the road
            NotConnectedError: If check_connection is True and the road is not connected to anything
            ValueError: If path_coords is not a set of two valid intersection coordinates
            CoordsBlockedError: If the position is already blocked by another road/other path building

    `build_settlement(self, player: katan_ai.katan.player.Player, coords: katan_ai.katan.board.coords.Coords, cost_resources: Optional[bool] = True, ensure_connected: Optional[bool] = True)`
    :   Build a settlement by the player given in the coords given, or raises an error if the input is invalid.

        Args:
            player: The player who is building the settlement
            coords: The coordinates to build the settlement at
            cost_resources: Whether to remove the resources required to build a settlement from the player's hands, and
                raise an error if they don't have them. Defaults to True
            ensure_connection: Whether to raise an error if the settlement would not be connected to a road owned by the same
                player. Defaults to True
        Raises:
            NotEnoughResourcesError: If check_resources is True and the player does not have enough resources
            NotConnectedError: If check_connection is True and the settlement would not be connected to any roads owned by the player

    `get_victory_points(self, player: katan_ai.katan.player.Player)`
    :   Get the number of victory points the player has.

        Args:
            player: The player to get the victory points for
        Returns:
            The number of victory points

    `move_robber(self, coords: katan_ai.katan.board.coords.Coords)`
    :   Move the robber to the coords specified.

        Args:
            coords: The coordinates of the hex to move the robber to
        Raises:
            ValueError: If the coordinates are not a valid hex

    `play_development_card(self, player: katan_ai.katan.player.Player, card: katan_ai.katan.development_card.DevelopmentCard)`
    :   Play a development card.

        Do not actually change the game state to play the card.
        Mainly just keep track of how many knight cards each player has played and may change who has the largest army

        Args:
            player: The player playing a development card
            card: The development card they are playing
        Raises:
            ValueError: If the player does not have the card

    `upgrade_settlement_to_city(self, player: katan_ai.katan.player.Player, coords: katan_ai.katan.board.coords.Coords, cost_resources: Optional[bool] = True)`
    :   Build a city from a settlement.

        Args:
            player: The player who is building the city
            coords: Where to build the city
            cost_resources: Whether to remove the resources from the player's hand
        Raises:
            NotEnoughResourcesError: If cost_resources is true and the player doesn't have enough resources
            ValueError: If coords is not a valid intersection
            RequiresSettlementError: If there is not a valid settlement at the intersection to upgrade
