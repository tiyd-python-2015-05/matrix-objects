from matrix_math import *
from nose.tools import raises


def is_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal
    even when they should be."""
    return abs(x - y) <= tolerance


m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])

q = Matrix([[1, 3, 0], [0, 2, 4]])

def test_shape_vectors():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert m.shape == (2,)
    assert v.shape == (3,)
    assert q.shape == (3, 2)

def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    x = Vector([1, 5, 4])
    assert v + w == [1, 5, 4]
    assert v + w == x
    assert u + y == [11, 21, 31]
    assert u + z == u


def test_vector_add_is_communicative():
    assert w + y == y + w

def test_vector_equality():
    assert not v == w
    assert v != w
    assert v == [1, 3, 0]

@raises(ShapeException)
def test_vector_add_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m + v


def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    q = Vector([1, 1, -4])
    p = Vector([-1, -1, 4])
    assert v - w == [1, 1, -4]
    assert v - w == q
    assert w - v == [-1, -1, 4]
    assert w - v == p
    assert y - z == y
    assert w - u == (z - (u - w))


@raises(ShapeException)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m - v


@raises(ShapeException)
def test_vector_mult_checks_scalar():
    """Shape rule: vector mult only by scalar."""
    m * v


def test_vector_multiply():
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """
    assert v * 0.5 == [0.5, 1.5, 0]
    assert m * 2 == [6, 8]


def test_magnitude():
    """
    magnitude([a b])  = sqrt(a^2 + b^2)

    magnitude(Vector) = Scalar
    """
    assert m.magnitude() == 5
    assert v.magnitude() == math.sqrt(10)
    assert y.magnitude() == math.sqrt(1400)
    assert z.magnitude() == 0
