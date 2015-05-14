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
    assert q.shape == (2, 3)

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
    assert m.magnitude() == 5
    assert v.magnitude() == math.sqrt(10)
    assert y.magnitude() == math.sqrt(1400)
    assert z.magnitude() == 0

def test_repr():
    assert repr(m) == "Vector: [3, 4]"

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
E = Matrix([[1, 2, 3],
     [3, 2, 1]])

def test_shape_matrices():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert A.shape == (3, 3)
    assert C.shape == (3, 2)
    assert D.shape == (2, 3)



def test_matrix_equality():
    assert D == E
    assert A != B

C_Result = Matrix([[3, 6], [6, 3], [3, 6]])

def test_matrix_scalar_multiply():
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]

    Matrix * Scalar = Matrix
    """
    assert C * 3 == C_Result


Test_Vec_A = Vector([2, 5, 4])
Test_Vec_B = Vector([1, 2, 3])
Test_Vec_C = Vector([3, 4])
Test_Vec_D = Vector([0, 1, 2])


def test_matrix_vector_multiply():
    """
    [[a b]   *  [x   =   [a*x+b*y
     [c d]       y]       c*x+d*y
     [e f]                e*x+f*y]

    Matrix * Vector = Vector
    """
    assert A * Test_Vec_A == [2, 5, 4]
    assert B * Test_Vec_B == [14, 32, 50]
    assert C * Test_Vec_C == [11, 10, 11]
    assert D * Test_Vec_D == [8, 4]


Test_Vec = Vector([1, 2 ,3])


@raises(ShapeException)
def test_matrix_vector_multiply_checks_shapes():
    """Shape Rule: The number of rows of the vector must equal the number of
    columns of the matrix."""
    C * Test_Vec


BC_Result = Matrix([[8, 10],
                [20, 25],
                [32, 40]])
CD_Result = Matrix([[7, 6, 5],
                [5, 6, 7],
                [7, 6, 5]])
DC_Result = Matrix([[8, 10],
                [8, 10]])

def test_matrix_matrix_multiply():
    """
    [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
     [c d]       [y z]]       [c*w+d*y c*x+d*z]
     [e f]                    [e*w+f*y e*x+f*z]]

    Matrix * Matrix = Matrix
    """
    assert A * B == B
    assert B * C == BC_Result
    assert C * D == CD_Result
    assert D * C == DC_Result


def test_matrix_col():
    """
           0 1  <- rows
       0 [[a b]]
       1 [[c d]]
       ^
     columns
    """
    assert A.matrix_col(0) == [1, 0, 0]
    assert B.matrix_col(1) == [2, 5, 8]
    assert D.matrix_col(2) == [3, 1]

# @raises(ShapeException)
# def test_matrix_matrix_multiply_checks_shapes():
#     """Shape Rule: The number of columns of the first matrix must equal the
#     number of rows of the second matrix."""
#     matrix_matrix_multiply(A, D)
#
