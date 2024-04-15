from cadquery.occ_impl.shapes import (
    vertex,
    segment,
    polyline,
    polygon,
    rect,
    circle,
    ellipse,
    face,
    plane,
    box,
    cylinder,
    sphere,
    torus,
    cone,
)

from pytest import approx
from math import pi

#%% primitives


def test_vertex():

    v = vertex((1, 2,))

    assert v.isValid()
    assert v.Center().toTuple() == approx((1, 2, 0))

    v = vertex(1, 2, 3)

    assert v.isValid()
    assert v.Center().toTuple() == approx((1, 2, 3))


def test_segment():

    s = segment((0, 0, 0), (0, 0, 1))

    assert s.isValid()
    assert s.Length() == approx(1)


def test_polyline():

    s = polyline((0, 0), (0, 1), (1, 1))

    assert s.isValid()
    assert s.Length() == approx(2)


def test_polygon():

    s = polygon((0, 0), (0, 1), (1, 1), (1, 0))

    assert s.isValid()
    assert s.IsClosed()
    assert s.Length() == approx(4)


def test_rect():

    s = rect(2, 1)

    assert s.isValid()
    assert s.IsClosed()
    assert s.Length() == approx(6)


def test_circle():

    s = circle(1)

    assert s.isValid()
    assert s.IsClosed()
    assert s.Length() == approx(2 * pi)


def test_ellipse():

    s = ellipse(3, 2)

    assert s.isValid()
    assert s.IsClosed()
    assert face(s).Area() == approx(6 * pi)


def test_plane():

    s = plane(1, 2)

    assert s.isValid()
    assert s.Area() == approx(2)


def test_box():

    s = box(1, 1, 1)

    assert s.isValid()
    assert s.Volume() == approx(1)


def test_cylinder():

    s = cylinder(2, 1)

    assert s.isValid()
    assert s.Volume() == approx(pi)


def test_sphere():

    s = sphere(2)

    assert s.isValid()
    assert s.Volume() == approx(4 / 3 * pi)


def test_torus():

    s = torus(10, 2)

    assert s.isValid()
    assert s.Volume() == approx(2 * pi ** 2 * 5)


def test_cone():

    s = cone(2, 1)

    assert s.isValid()
    assert s.Volume() == approx(1 / 3 * pi)

    s = cone(2, 1, 1)

    assert s.isValid()
    assert s.Volume() == approx(1 / 3 * pi * (1 + 0.25 + 0.5))


#%% bool ops
def test_operators():

    b1 = box(1, 1, 1)  # small box
    b2 = box(2, 2, 2)  # large box
    f = plane(3, 3)  # face
    e = segment((-2, 0), (2, 0))  # edge

    assert (b2 - b1).Volume() == approx(8 - 1)

    assert (b2 * b1).Volume() == approx(1)
    assert (b1 * f).Area() == approx(1)
    assert (b1 * e).Length() == approx(1)
    assert (f * e).Length() == approx(3)

    assert (b2 + b1).Volume() == approx(8)

    assert len((b1 / f).Solids()) == 2
