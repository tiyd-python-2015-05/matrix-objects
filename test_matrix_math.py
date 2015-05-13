from matrix_math import *
import math
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

def test_hard_mode_vector():
    Vector([1, 2]) + Vector([0, 4])
    Vector([1, 2]) - Vector([0, 4])
    Vector([1, 2]) * 3

    assert Vector([1, 2]) == Vector([1, 2]) # results in True


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

def test_magnitude():
    """
    magnitude([a b])  = sqrt(a^2 + b^2)

    magnitude(Vector) = Scalar
    """
    assert m.magnitude() == 5
    assert v.magnitude() == math.sqrt(10)
    assert y.magnitude() == math.sqrt(1400)
    assert z.magnitude() == 0




def test_shape_matrices():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert A.shape() == (3, 3)
    assert C.shape() == (3, 2)
    assert D.shape() == (2, 3)
def test_matrix_scalar_multiply():
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]

    Matrix * Scalar = Matrix
    """
    assert C * 3 == Matrix([[3, 6],
                            [6, 3],
                            [3, 6]])


def test_matrix_vector_multiply():
    """
    [[a b]   *  [x   =   [a*x+b*y
     [c d]       y]       c*x+d*y
     [e f]                e*x+f*y]

    Matrix * Vector = Vector
    """
    assert A * Vector([2, 5, 4]) == Vector([2, 5, 4])
    assert B * Vector([1, 2, 3]) == Vector([14, 32, 50])
    assert C * Vector([3, 4]) == Vector([11, 10, 11])
    assert D * Vector([0, 1, 2]) == Vector([8, 4])


@raises(ShapeException)
def test_matrix_vector_multiply_checks_shapes():
    """Shape Rule: The number of rows of the vector must equal the number of
    columns of the matrix."""
    C * Vector([1, 2, 3])


def test_matrix_matrix_multiply():
    """
    [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
     [c d]       [y z]]       [c*w+d*y c*x+d*z]
     [e f]                    [e*w+f*y e*x+f*z]]

    Matrix * Matrix = Matrix
    """
    assert A * B == B
    assert B * C == Matrix([[8, 10],
                                            [20, 25],
                                            [32, 40]])
    assert C * D == Matrix([[7, 6, 5],
                                            [5, 6, 7],
                                            [7, 6, 5]])
    assert D * C == Matrix([[8, 10], [8, 10]])


@raises(ShapeException)
def test_matrix_matrix_multiply_checks_shapes():
    """Shape Rule: The number of columns of the first matrix must equal the
    number of rows of the second matrix."""
    A * D


def test_hard_mode_matrix():
    Matrix([[0, 1], [1, 0]]) + Matrix([[1, 1], [0, 0]])
    Matrix([[0, 1], [1, 0]]) - Matrix([[1, 1], [0, 0]])
    Matrix([[0, 1], [1, 0]]) * 3
    Matrix([[0, 1], [1, 0]]) * Vector([1, 2])
    Matrix([[1, 1, 1], [0, 0, 0]]) * Matrix([[1, 1], [2, 2], [3, 3]])

    assert not Matrix([[0, 1], [1, 0]]) == Matrix([[1, 1], [0, 0]]) # results in False
