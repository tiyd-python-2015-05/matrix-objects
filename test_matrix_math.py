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

def test_matrix_class():
    v = Vector([1, 5])
    assert v.shape() == (2,)

def test_matrix_shape():
    m = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    assert m.shape() == (3,3)
    m = Matrix([[1,2],[3,4],[5,6]])
    assert m.shape() == (3,2)
