from matrix import Matrix, ShapeException

import nose
from nose.tools import raises

def test_zeroes():
    zeroes = Matrix.zeroes((3,2))
    assert zeroes == Matrix([[0, 0]]*3)

@raises(ShapeException)
def test_zeroes_bad_shape():
    Matrix.zeroes((11,2,3))

@raises(ShapeException)
def test_matrix_bad_shape():
    Matrix([[0,0,0],[0,0]])

class Zeroes:
    def randint(self, start, end):
        return 0

class Ones:
    def randint(self, start, end):
        return 1

class Count:
    def __init__(self):
        self.int = 0

    def randint(self, start, end):
        self.int+=1
        return self.int

def test_random():
    shape = (3, 5)
    assert Matrix.random(shape, 0, 5, Zeroes()) == Matrix.zeroes(shape)

    assert Matrix.random(shape, 0, 5, Ones()) == Matrix([[1, 1, 1, 1, 1]]*3)

    assert Matrix.random(shape, 0, 5, Count()) == Matrix([[1, 2, 3, 4, 5],
                                                          [6, 7, 8, 9, 10],
                                                          [11, 12, 13, 14 ,15]])

def test_matrix_mult():
    identity = Matrix([[1,0,0],
                       [0,1,0],
                       [0,0,1]])

    a_mat = Matrix([[1,3,2],
                    [2,3,1],
                    [3,1,2]])

    assert identity * a_mat == a_mat * identity
    assert identity * a_mat == a_mat

#def test_bad_matrix_mult():



if __name__ == '__main__':
    nose.main()
