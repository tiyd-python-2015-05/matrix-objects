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
    assert shape_vectors(m == (2,)
    assert shape_vectors(v) == (3,)
    assert shape_vectors(q) == (3, 2)

def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    assert v + w == [1, 5, 4]
    assert u + y == [11, 21, 31]
    assert u + z == u


def test_vector_add_is_communicative():
    assert w + y == y + w


@raises(ShapeException)
def test_vector_add_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m + v


# def test_vector_sub():
#     """
#     [a b]  - [c d]  = [a-c b-d]
#
#     Matrix + Matrix = Matrix
#     """
#     assert vector_sub(v, w) == [1, 1, -4]
#     assert vector_sub(w, v) == [-1, -1, 4]
#     assert vector_sub(y, z) == y
#     assert vector_sub(w, u) == vector_sub(z, vector_sub(u, w))
#
#
# @raises(ShapeException)
# def test_vector_sub_checks_shapes():
#     """Shape rule: the vectors must be the same size."""
#     vector_sub(m, v)
#
