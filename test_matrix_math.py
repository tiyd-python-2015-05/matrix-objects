from matrix_math import *
from nose.tools import raises


m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])


def test_shape_vectors():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert m.shape() == (2,)
    assert v.shape() == (3,)
    assert w.shape() == (3,)

@raises(TypeError)
def test_vectors_with_differing_length_cannot_be_added():
    m + v
    n + y

def test_vector_add():
    """
    [a b]  + [c d]  = [a+c b+d]
    Matrix + Matrix = Matrix
    """
    assert v + w == [1, 5, 4]
    assert u + y == [11, 21, 31]
    assert u == u

@raises(TypeError)
def test_vectors_with_differing_length_cannot_be_subtracted():
    m - v
    z - n

def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]
    Matrix + Matrix = Matrix
    """
    assert v - w == [1, 1, -4]
    assert w - v == [-1, -1, 4]
    assert y  == y
    assert w - u == [-1, 1, 3]

def test_dot():
    """
    dot([a b], [c d])   = a * c + b * d
    dot(Vector, Vector) = Scalar
    """
    assert Vector.vector_dot(w, y) == 160
    assert Vector.vector_dot(m, n) == 15
    assert Vector.vector_dot(u, z) == 0


@raises(TypeError)
def test_dot_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    Vector.vector_dot(v, m)


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


def test_shape_matrices():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert A.shape() == (3, 3)
    assert C.shape() == (3, 2)
    assert D.shape() == (2, 3)


def test_matrix_add():
    """
    [a b]  + [c d]  = [a+c b+d]
    [w x]  + [y z]  = [w+y x+z]
    Matrix + Matrix = Matrix
    """
    assert A + B == [[2, 2, 3],
                     [4, 6, 6],
                     [7, 8, 10]]

def test_matrix_scalar_multiply():
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]
    Matrix * Scalar = Matrix
    """
    assert C * 3 == [[3, 6],
                     [6, 3],
                     [3, 6]]


def test_transpose():

    assert A == [[0, 0, 1],
                 [0, 1, 0],
                 [1, 0, 0]]
