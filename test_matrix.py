from matrix import Matrix, ShapeException

import nose
from nose.tools import raises

def test_zeroes():
    zeroes = Matrix.zeroes((3,2))
    assert zeroes.values == [[0, 0]]*3

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
    assert Matrix.random(shape, Zeroes()) == Matrix.zeroes(shape)
    print(Matrix.random(shape, Ones()).values)
    assert Matrix.random(shape, Ones()) == Matrix([[1, 1, 1, 1, 1]]*3)
    assert Matrix.random(shape, Count()) == Matrix([[1, 2, 3, 4, 5],
                                             [6, 7, 8, 9, 10],
                                             [11, 12, 13, 14 ,15]])

if __name__ == '__main__':
    nose.main()
