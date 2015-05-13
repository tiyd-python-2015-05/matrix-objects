from matrix_math import ShapeException, Vector, Matrix
from nose.tools import raises
import math


def test_vector_has_content():
    v1 = Vector([1, 2, 3])
    assert v1.values == [1, 2, 3]


def test_vector_has_shape():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2])
    assert v1.shape == (3,)
    assert v2.shape == (2,)


def test_vector_equality():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    assert v1 == v2


def test_can_add_vector_objects():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1 + v2 == Vector([5, 7, 9])
    assert v2 + v1 == Vector([5, 7, 9])


@raises(ShapeException)
def test_vector_add_raises_shape_exception():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2])
    v1 + v2


def test_can_subtract_vector_objects():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1 - v2 == Vector([-3, -3, -3])
    assert v2 - v1 == Vector([3, 3, 3])


@raises(ShapeException)
def test_vector_subtract_raises_shape_exception():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2])
    v1 - v2


def test_vector_multiplication():
    v1 = Vector([1, 2, 3])
    assert v1 * 2 == Vector([2, 4, 6])
    assert v1 * 2 == Vector([2, 4, 6])


def test_vector_dot():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1.dot(v2) == 32


@raises(ShapeException)
def test_vector_dot_raises_shape_exception():
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2])
    v1.dot(v2)


def test_vector_magnitude():
    v1 = Vector([3, 4])
    v2 = Vector([1, 3, 0])
    v3 = Vector([10, 20, 30])
    v4 = Vector([0, 0, 0])
    assert v1.mag() == 5
    assert v2.mag() == math.sqrt(10)
    assert v3.mag() == math.sqrt(1400)
    assert v4.mag() == 0


def test_vector_works_with_floats():
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([4.0, 5.0, 6.0])
    assert v1 + v2 == Vector([5.0, 7.0, 9.0])
    assert v2 + v1 == Vector([5.0, 7.0, 9.0])


@raises(ValueError)
def test_vector_creation():
    v1 = Vector([1, 2, "3"])

m1 = Matrix([[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]])

m2 = Matrix([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

m3 = Matrix([[1, 2],
             [2, 1],
             [1, 2]])

m4 = Matrix([[1, 2, 3],
             [3, 2, 1]])

def test_matrix_has_content():
    assert m1.values == [[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]]


def test_matrix_has_shape():
    assert m1.shape == (3,3)
    assert m3.shape == (3,2)
    assert m4.shape == (2,3)


def test_matrix_equality():
    assert m1 == Matrix([[1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])


def test_matrix_addition():
    assert m1 + m2 == Matrix([[2, 2, 3], [4, 6, 6], [7, 8, 10]])


@raises(ShapeException)
def test_matrix_add_raises_ShapeException():
    m1 + m3


def test_matrix_subtraction():
    assert m2 - m1 == Matrix([[0, 2, 3], [4, 4, 6], [7, 8, 8]])


@raises(ShapeException)
def test_matrix_sub_raises_ShapeException():
    m1 - m3


def test_matrix_scalar_multiply():
    assert m1 * 3 == Matrix([[3, 0, 0],
                             [0, 3, 0],
                             [0, 0, 3]])
    assert m3 * 3 == Matrix([[3, 6],
                             [6, 3],
                             [3, 6]])
v1 = Vector([2, 5, 4])
v2 = Vector([1, 2, 3])
v3 = Vector([3, 4])
v4 = Vector([0, 1, 2])
def test_matrix_vector_multiply():
    assert m1 * v1 == Vector([2, 5, 4])
    assert v1 * m1 == Vector([2, 5, 4])
    assert m2 * v2 == Vector([14, 32, 50])
    assert m3 * v3 == Vector([11, 10, 11])
    assert m4 * v4 == Vector([8, 4])


@raises(ShapeException)
def test_matrix_vector_multiply_raises_ShapeException():
    m1 * v3


def test_matrix_transpose():
    assert m2.transpose() == Matrix([[1, 4, 7],
                                     [2, 5, 8],
                                     [3, 6, 9]])


def test_matrix_matrix_multiply():
    assert m1 * m2 == m2
    assert m2 * m3 == Matrix([[8, 10],
                              [20, 25],
                              [32, 40]])
    assert m3 * m4 == Matrix([[7, 6, 5],
                              [5, 6, 7],
                              [7, 6, 5]])
    assert m4 * m3 == Matrix([[8, 10],
                              [8, 10]])
    assert Matrix([[1,2],[3,4]]) * Matrix([[1, 2, 3], [4, 5, 6]]) == \
                                            Matrix([[9, 12, 15], [19, 26, 33]])

@raises(ShapeException)
def test_matrix_matrix_multiply_checks_shapes():
    m1 * m4


@raises(ValueError)
def test_matrix_creation():
    #m1 = Matrix([[3, 4, 5], [2, 5, 7], [1, 2, "3"]])
    m2 = Matrix([[3, 4, 5], [2], [1, 2, 3]])

def test_from_function():
    def diagonal_ones(x, y):
        if x == y:
            return 1
        else:
            return 0
    assert Matrix.from_function(2, 2, diagonal_ones) == Matrix([[1, 0],
                                                                [0, 1]])
