from matrix_objects import *
from nose.tools import raises

m = Vector([1,2,3])
n = Vector([4,5,6])
y = Vector([2, 3])
z = Vector([10,100])


def test_shape_of():
    v3 = Vector([1])
    assert m.shape_of()==(3,)
    assert y.shape_of() == (2,)
    assert v3.shape_of() == (1,)



def test_vector_add():


    assert m + n == Vector([5,7,9])
    assert y + z == Vector([12, 103])

def test_vector_sub():
    assert m-n == Vector([-3,-3,-3])
    assert z-y == Vector([8,97])

def test_vec_multiply():

    assert m * 3 == Vector([3,6,9])
    assert z * 5 == Vector([50, 500])
    #assert v2.vector_add(w,y) == [10,22,34]
