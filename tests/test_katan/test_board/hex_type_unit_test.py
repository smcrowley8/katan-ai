"""Unit tests for hex_type of katanAI.katan.board module"""

from katan_ai.katan.board import HexType

def test_forest_hex_type():
    forest_hex = HexType(0)
    assert(str(forest_hex.get_resource()) == "Lumber")

def test_hills_hex_type():
    hills_hex_type = HexType(1)
    assert(str(hills_hex_type.get_resource()) == "Brick")

def test_pasture_hex_type():
    pasture_hex_type = HexType(2)
    assert(str(pasture_hex_type.get_resource()) == "Wool")

def test_fields_hex_type():
    fields_hex_type = HexType(3)
    assert(str(fields_hex_type.get_resource()) == "Grain")

def test_mountains_hex_type():
    mountains_hex_type = HexType(4)
    assert(str(mountains_hex_type.get_resource()) == "Ore")

def test_desert_hex_type():
    desert_hex_type = HexType(5)
    assert(str(desert_hex_type.get_resource()) == 'None')