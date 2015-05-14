
from matrix_object import *
from nose.tools import raises

m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])

q = Vector([[1, 3, 0], [0, 2, 4]])

def test_shape():

  assert m.shape == (len(m.row),)

def test_vector_equality():

    assert m == [3,4]
    assert m == m

# def test_vector_repr():
#     assert repr(m) == "Vector: [3, 4]"

def test_vector_add():

    assert v + w == Vector([1, 5, 4])
    assert v + w == [1, 5, 4]

def test_vector_sub():

    assert v - w == [1, 1, -4]
    assert w - v == [-1, -1, 4]
    assert y - z == y

# @raises(ShapeException)
# def test_for_exception():
#     m * v

def test_vector_mul_sum():

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

# @raises(ShapeException)
def test_dot():
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    assert w.dot(y)  == 160
    assert m.dot(n)  == 15
    assert u.dot(z) == 0

A = Matrix(
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
     )
B = Matrix(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
     )
C = Matrix(
    [[1, 2],
     [2, 1],
     [1, 2]]
     )
D = Matrix(
    [[1, 2, 3],
     [3, 2, 1]]
     )

def test_shape_matrices():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""

    assert A.shape == (3, 3)
    assert C.shape == (3, 2)
    assert D.shape == (2, 3)


def test_matrix_scalar_multiply():
    """
    [[a b]   *  Z   =   [[a*Z b*Z]
     [c d]]              [c*Z d*Z]]

    Matrix * Scalar = Matrix
    """
    C_result = Matrix([[3, 6],[6, 3],[3, 6]])
    assert C * 3 == C_result
    assert C * 3 == [[3, 6],[6, 3],[3, 6]]

def test_matrix_matrix_multiply():
    """
    [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
     [c d]       [y z]]       [c*w+d*y c*x+d*z]
     [e f]]                   [e*w+f*y e*x+f*z]]

    Matrix * Matrix = Matrix
    """
    assert A * B == B
    assert B * C == [[8, 10],
                    [20, 25],
                    [32, 40]]

    assert C * D == [[7, 6, 5],
                    [5, 6, 7],
                    [7, 6, 5]]

    assert D * C == [[8, 10],
                    [8, 10]]
