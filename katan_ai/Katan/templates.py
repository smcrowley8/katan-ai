"""Repository of templates other classes will use for customizing initialization"""

# a basic board is 7x7 in 2d to account for a 5 length middle row and a null border of hexes
BASIC_BOARD_SETUP = [
    [-1, -1, -1, -1, -1, -1, -1],  # shifted left conceptually
    [-1, -1, 0, 0, 0, -1, -1],  # shifted right conceptually
    [-1, 0, 0, 0, 0, -1, -1],  # SL
    [-1, 0, 0, 0, 0, 0, -1],  # SR
    [-1, 0, 0, 0, 0, -1, -1],  # SL
    [-1, -1, 0, 0, 0, -1, -1],  # SR
    [-1, -1, -1, -1, -1, -1, -1],  # SL
]
"""=>
    nulllllllllllllllllllllllllll
    null__ empty, empty, empty, null___
    nul, empty, empty, empty, empty, nul
    empty, empty, empty, empty, empty,
    nul, empty, empty, empty, empty, nul
    null__ empty, empty, empty, null___
"""
