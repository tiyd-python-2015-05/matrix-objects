from matrix_math import *
from nose.tools import raises

def test_matrix_class():
    m = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

def test_vector_class():
    v = Vector([1, 5])

@raises(ValueError)
def test_2d_vector_exception():
    v = Vector([[0, 1, 0], [1, 0, 0], [0, 0, 1]])

@raises(ValueError)
def test_empty_vector_exception():
    v = Vector([])

@raises(ValueError)
def test_1d_matrix_exception():
    m = Matrix([1,5])

@raises(ValueError)
def test_empty_matrix_exception():
    v = Matrix([])


m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])

A = Matrix([[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]])
B = Matrix([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]])
C = Matrix([[1, 2],
     [2, 1],
     [1, 2]])
D = Matrix([[1, 2, 3],
     [3, 2, 1]])

def test_matrix_class_and_shape():
    assert m.shape() == (2,)
    assert v.shape() == (3,)

def test_matrix_shape():
    m = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    assert m.shape() == (3,3)
    m = Matrix([[1,2],[3,4],[5,6]])
    assert m.shape() == (3,2)
    assert A.shape() == (3, 3)
    assert C.shape() == (3, 2)
    assert D.shape() == (2, 3)
def test_vector_eq():
    p = Vector([3,4])
    assert m == p

def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    assert v + w == Vector([1, 5, 4])
    assert u + y == Vector([11, 21, 31])
    assert u + z == u

def test_vector_add_is_communicative():
    assert w + y == y + w

def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    assert v - w == Vector([1, 1, -4])
    assert w - v == Vector([-1, -1, 4])
    assert y - z == y
    assert w - u == (z - (u - w))


@raises(ShapeException)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m - v

def test_dot():
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    assert w.dot(y) == 160
    assert m.dot(n) == 15
    assert u.dot(z) == 0


@raises(ShapeException)
def test_dot_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    v.dot(m)


def test_vector_multiply():
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """
    assert v * 0.5 == Vector([0.5, 1.5, 0])
    assert m * 2 == Vector([6, 8])




"""
def test_matrix_add():
    assert False
def test_matrix_sub():
    assert False
"""
