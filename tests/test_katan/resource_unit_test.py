"""Unit tests for the resource class of the katan module"""

from katan_ai.katan.resource import Resource

def test_wood_resource():
    wood_resouce = Resource(0)
    assert(str(wood_resouce) == "Lumber")

def test_brick_resource():
    brick_resouce = Resource(1)
    assert(str(brick_resouce) == "Brick")

def test_wool_resource():
    wool_resouce = Resource(2)
    assert(str(wool_resouce) == "Wool")

def test_grain_resource():
    grain_resouce = Resource(3)
    assert(str(grain_resouce) == "Grain")

def test_ore_resource():
    ore_resouce = Resource(4)
    assert(str(ore_resouce) == "Ore")