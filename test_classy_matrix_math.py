from classy_matrix_math import Vector, ShapeException, Matrix
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

a = Matrix([[1,0],
            [2,1],
            [1,1]])

b = Matrix([[2,1,2],
            [1,1,1],
            [1,1,2]])

def test_shape_vectors():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert m.shape() == (2,)
    assert v.shape() == (3,)
    assert Vector([1]).shape() == (1,)


def test_vector_can_be_added_with_std_operator():
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    assert v + w == Vector([1, 5, 4])
    assert u + y == Vector([11, 21, 31])
    assert u + z == u


def test_vector_add_is_communicative():
    assert w + y == y + w


@raises(ShapeException)
def test_vector_add_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m + v


def test_vector_sub():
    """
    [a b]  - [c d]  = [a-c b-d]

    Matrix + Matrix = Matrix
    """
    assert v - w == Vector([1, 1, -4])
    assert w - v == Vector([-1, -1, 4])
    assert y - z == y
    assert w - u == z - (u - w)


@raises(ShapeException)
def test_vector_sub_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m - w

def test_vector_times():

    assert v * w == Vector([0, 6, 0])
    assert w * v == Vector([0, 6, 0])
    assert y * z == z

@raises(ShapeException)
def test_vector_times_checks_shapes():
    """Shape rule: the vectors must be the same size."""
    m * w



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
    assert v.vector_multiply(0.5) == [0.5, 1.5, 0]
    assert m.vector_multiply(2) == [6, 8]


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

def test_matrix_shape():

    assert A.matrix_shape() == (3, 3)
    assert C.matrix_shape() == (3, 2)
    assert D.matrix_shape() == (2, 3)


def test_matrix_row():
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    assert A.matrix_row(0) == [1, 0, 0]
    assert B.matrix_row(1) == [4, 5, 6]
    assert C.matrix_row(2) == [1, 2]


def test_matrix_col():
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    assert matrix_col(A, 0) == [1, 0, 0]
    assert matrix_col(B, 1) == [2, 5, 8]
    assert matrix_col(D, 2) == [3, 1]


# def test_matrix_scalar_multiply():
#     """
#     [[a b]   *  Z   =   [[a*Z b*Z]
#      [c d]]              [c*Z d*Z]]
#
#     Matrix * Scalar = Matrix
#     """
#     assert matrix_scalar_multiply(C, 3) == [[3, 6],
#                                             [6, 3],
#                                             [3, 6]]
#
#
# def test_matrix_vector_multiply():
#     """
#     [[a b]   *  [x   =   [a*x+b*y
#      [c d]       y]       c*x+d*y
#      [e f]                e*x+f*y]
#
#     Matrix * Vector = Vector
#     """
#     assert matrix_vector_multiply(A, [2, 5, 4]) == [2, 5, 4]
#     assert matrix_vector_multiply(B, [1, 2, 3]) == [14, 32, 50]
#     assert matrix_vector_multiply(C, [3, 4]) == [11, 10, 11]
#     assert matrix_vector_multiply(D, [0, 1, 2]) == [8, 4]
#
#
# @raises(ShapeException)
# def test_matrix_vector_multiply_checks_shapes():
#     """Shape Rule: The number of rows of the vector must equal the number of
#     columns of the matrix."""
#     matrix_vector_multiply(C, [1, 2, 3])
#
#
# def test_matrix_matrix_multiply():
#     """
#     [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
#      [c d]       [y z]]       [c*w+d*y c*x+d*z]
#      [e f]                    [e*w+f*y e*x+f*z]]
#
#     Matrix * Matrix = Matrix
#     """
#     assert matrix_matrix_multiply(A, B) == A
#     assert matrix_matrix_multiply(B, C) == [[8, 10],
#                                             [20, 25],
#                                             [32, 40]]
#     assert matrix_matrix_multiply(C, D) == [[7, 6, 5],
#                                             [5, 6, 7],
#                                             [7, 6, 5]]
#     assert matrix_matrix_multiply(D, C) == [[8, 10], [8, 10]]
#
#
# @raises(ShapeException)
# def test_matrix_matrix_multiply_checks_shapes():
#     """Shape Rule: The number of columns of the first matrix must equal the
#     number of rows of the second matrix."""
#     matrix_matrix_multiply(A, D)
