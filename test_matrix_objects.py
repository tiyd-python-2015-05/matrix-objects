from matrix_objects import Vector,Matrix,ShapeException
from nose.tools import raises
import math

a = Vector([1,2,3])
b = Vector([0,4,3])
c = Vector([2,4])
d = Vector([3,1])
e = Vector([1,-3])
f = Vector([4,3,1])
g = Vector([3,3,1])

def test_vector_shape():
    assert Vector.shape(a) == (3,)
    assert Vector.shape(b) == (3,)
    assert Vector.shape(c) == (2,)

def test_vector_equality():
    assert a == Vector([1,2,3])

def test_vector_inequality():
    assert a != Vector([1,2,4])

@raises(TypeError)
def test_vector_equality_error():
    assert a == 4

def test_vector_add():
    assert a + b == [1, 6, 6]
    assert c + d == [5, 5]
    assert Vector([0,1,2]) + Vector([1,1,1]) == a

def test_vector_add_is_communicative():
    assert a + b == b + a

@raises(ShapeException)
def test_vector_add_checks_shapes():
    a + d

def test_vector_sub():
    assert a - b == [1,-2,0]
    assert c - d == [-1,3]
    assert d - c == e

@raises(ShapeException)
def test_vector_sub_checks_shapes():
    a - d

def test_dot():
    assert Vector.dot(a, b) == 17
    assert Vector.dot(c, d) == 10
    assert Vector.dot(f, g) == 22

@raises(ShapeException)
def test_dot_checks_shapes():
    Vector.dot(a, c)

def test_vector_multiply():
    assert a * 0.5 == [0.5, 1, 1.5]
    assert b * 2 == [0, 8, 6]

def test_magnitude():
    assert Vector.magnitude(a) == math.sqrt(14)
    assert Vector.magnitude(b) == 5
    assert Vector.magnitude(c) == math.sqrt(20)
    assert Vector.magnitude(d) == math.sqrt(10)

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
E = Matrix([[2, 1, 1],
            [2, 3, 4],
            [1, 6, 4]])
F = Matrix([[7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]])

def test_matrix_addition():
    assert A + B == [[2, 2, 3], [4, 6, 6], [7, 8, 10]]
    assert A + E == [[3, 1, 1], [2, 4, 4], [1, 6, 5]]

def test_matrix_subtraction():
    assert A - B == [[0, -2, -3], [-4, -4, -6], [-7, -8, -8]]
    assert B - E == [[-1, 1, 2], [2, 2, 2], [6, 2, 5]]

@raises(ShapeException)
def test_dot_checks_shapes():
    A + C

@raises(ShapeException)
def test_dot_checks_shapes():
    A - C

def test_matrix_scalar_multiply():
    assert C * 3 == [[3, 6], [6, 3], [3, 6]]

def test_matrix_vector_multiply():
    assert A * Vector([2, 5, 4]) == [2, 5, 4]
    assert B * Vector([1, 2, 3]) == [14, 32, 50]
    assert C * Vector([3, 4]) == [11, 10, 11]
    assert D * Vector([0, 1, 2]) == [8, 4]

@raises(ShapeException)
def test_matrix_vector_multiply_checks_shapes():
    C * Vector([1, 2, 3])

def test_matrix_matrix_multiply():
    assert A * B == B
    assert B * C == [[8, 10],
                     [20, 25],
                     [32, 40]]
    assert C * D == [[7, 6, 5],
                     [5, 6, 7],
                     [7, 6, 5]]
    assert D * C == [[8, 10], [8, 10]]


@raises(ShapeException)
def test_matrix_matrix_multiply_checks_shapes():
    A * D

def test_matrix_rotation():
    assert Matrix.rotate_matrix(B) == F
    assert Matrix.rotate_matrix(C) == [[1, 2, 1], [2, 1, 2]]


def test_static_method():
    assert Matrix.newMat(4) == Matrix([[0,0,0], [0,0,0], [0,0,0], [0,0,0]])
