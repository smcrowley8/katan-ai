import random

from katan_ai.katan import Game
from katan_ai.katan.board import RandomBoard

game = Game(RandomBoard())

pOne = game.players[0]
settlement_coords = game.board.get_valid_settlement_coords(
    player=pOne, ensure_connected=False
)
game.build_settlement(
    player=pOne,
    coords=random.choice(list(settlement_coords)),
    cost_resources=False,
    ensure_connected=False,
)
print(game.board)
