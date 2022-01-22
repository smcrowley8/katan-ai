"""Library of hex methods for the hex tile"""
# type: ignore[code, ...]
from __future__ import annotations

import collections
import math
from typing import Tuple

# Define the x y point for pixels
Point = collections.namedtuple("Point", ["x", "y"])
# q, r is angle and radias?
Axial_Point = collections.namedtuple("Axial_Point", ["q", "r"])
#
_Hex = collections.namedtuple("_Hex", ["q", "r", "s"])


def Hex(q: float, r: float, s: float) -> _Hex:
    """Return an instance of a hex"""
    assert not (round(q + r + s) != 0), "q + r + s must be 0"
    return _Hex(q, r, s)


def Axial_Hex(axialPoint: Axial_Point) -> _Hex:
    """Add function to create Hex from Axial Coordinates and an axial point as input"""
    s = -axialPoint.q - axialPoint.r
    assert not (round(axialPoint.q + axialPoint.r + s) != 0), "q + r + s must be 0"
    return _Hex(axialPoint.q, axialPoint.r, s)


def hex_add(a: _Hex, b: _Hex) -> _Hex:
    """add two hex tuples together"""
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)


def hex_subtract(a: _Hex, b: _Hex) -> _Hex:
    """subtract two axial coords"""
    return Hex(a.q - b.q, a.r - b.r, a.s - b.s)


def hex_scale(a: _Hex, k: _Hex) -> _Hex:
    """scale axial point by k"""
    return Hex(a.q * k, a.r * k, a.s * k)


def hex_rotate_left(a: _Hex) -> _Hex:
    """q->r->s->q"""
    return Hex(-a.s, -a.q, -a.r)


def hex_rotate_right(a: _Hex) -> _Hex:
    """r->q->s->r"""
    return Hex(-a.r, -a.s, -a.q)


"""
Hex directions -> the 6 hex tiles surrounding this one
"""

hex_directions = [
    Hex(1, 0, -1),
    Hex(1, -1, 0),
    Hex(0, -1, 1),
    Hex(-1, 0, 1),
    Hex(-1, 1, 0),
    Hex(0, 1, -1),
]


def hex_direction(direction: int) -> _Hex:
    """index of deriction?"""
    return hex_directions[direction]


def hex_neighbor(hex: _Hex, direction: int) -> _Hex:
    """checks if neighbor has occupied hex"""
    return hex_add(hex, hex_direction(direction))


hex_diagonals = [
    Hex(2, -1, -1),
    Hex(1, -2, 1),
    Hex(-1, -1, 2),
    Hex(-2, 1, 1),
    Hex(-1, 2, -1),
    Hex(1, 1, -2),
]


def hex_diagonal_neighbor(hex: _Hex, direction: int) -> _Hex:
    """checks diagnoal neighbor"""
    return hex_add(hex, hex_diagonals[direction])


def hex_length(hex: _Hex) -> int:
    """check absolute length of path"""
    return (abs(hex.q) + abs(hex.r) + abs(hex.s)) // 2


def hex_distance(a: _Hex, b: _Hex) -> int:
    """vertex distance"""
    return hex_length(hex_subtract(a, b))


def hex_round(h: _Hex) -> _Hex:
    """"""
    qi = int(round(h.q))
    ri = int(round(h.r))
    si = int(round(h.s))
    q_diff = abs(qi - h.q)
    r_diff = abs(ri - h.r)
    s_diff = abs(si - h.s)
    if q_diff > r_diff and q_diff > s_diff:
        qi = -ri - si
    else:
        if r_diff > s_diff:
            ri = -qi - si
        else:
            si = -qi - ri
    return Hex(qi, ri, si)


# Linear interpolation between 2 hexes
def hex_lerp(a: _Hex, b: _Hex, t: float) -> _Hex:
    """"""
    return Hex(
        a.q * (1.0 - t) + b.q * t, a.r * (1.0 - t) + b.r * t, a.s * (1.0 - t) + b.s * t
    )


def hex_linedraw(a: _Hex, b: _Hex) -> list:
    """"""
    N = hex_distance(a, b)
    a_nudge = Hex(a.q + 1e-06, a.r + 1e-06, a.s - 2e-06)
    b_nudge = Hex(b.q + 1e-06, b.r + 1e-06, b.s - 2e-06)
    results = []
    step = 1.0 / max(N, 1)
    for i in range(0, N + 1):
        results.append(hex_round(hex_lerp(a_nudge, b_nudge, step * i)))
    return results


# Specify Orientation and layout for Hex <-> Pixel conversion
Orientation = collections.namedtuple(
    "Orientation", ["f0", "f1", "f2", "f3", "b0", "b1", "b2", "b3", "start_angle"]
)

layout_pointy = Orientation(
    math.sqrt(3.0),
    math.sqrt(3.0) / 2.0,
    0.0,
    3.0 / 2.0,
    math.sqrt(3.0) / 3.0,
    -1.0 / 3.0,
    0.0,
    2.0 / 3.0,
    0.5,
)
layout_flat = Orientation(
    3.0 / 2.0,
    0.0,
    math.sqrt(3.0) / 2.0,
    math.sqrt(3.0),
    2.0 / 3.0,
    0.0,
    -1.0 / 3.0,
    math.sqrt(3.0) / 3.0,
    0.0,
)

# Layout has the orientation, size and origin
Layout = collections.namedtuple("Layout", ["orientation", "size", "origin"])


def hex_to_pixel(layout: Layout, h: _Hex) -> Point:
    """Function to covert axial hex coordinates to pixel"""
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    x = (M.f0 * h.q + M.f1 * h.r) * size.x
    y = (M.f2 * h.q + M.f3 * h.r) * size.y
    return Point(x + origin.x, y + origin.y)


def pixel_to_hex(layout: Layout, p: Point) -> _Hex:
    """Function to convert pixel coordinates to Hex"""
    M = layout.orientation
    size = layout.size
    origin = layout.origin
    pt = Point((p.x - origin.x) / size.x, (p.y - origin.y) / size.y)
    q = M.b0 * pt.x + M.b1 * pt.y
    r = M.b2 * pt.x + M.b3 * pt.y
    return Hex(q, r, -q - r)


def hex_corner_offset(layout: Layout, corner: int) -> Point:
    """Get the corner offset depending on the layout (using start angle)"""
    M = layout.orientation
    size = layout.size
    angle = 2.0 * math.pi * (M.start_angle - corner) / 6.0
    return Point(size.x * math.cos(angle), size.y * math.sin(angle))


def polygon_corners(layout: Layout, h: _Hex) -> list:
    """Get the corners of the Polygon in pixel coordinates"""
    corners = []
    center = hex_to_pixel(layout, h)
    for i in range(0, 6):
        offset = hex_corner_offset(layout, i)
        corners.append(
            Point(round(center.x + offset.x, 2), round(center.y + offset.y, 2))
        )
    return corners
