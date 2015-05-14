from vector import Vector, ShapeException

from nose.tools import raises
import nose


def test_zeroes():
    zeroes = Vector.zeroes(10)
    assert zeroes.values == [0] * 10


def test_check_shape():
    vect = Vector([1, 2, 3])
    assert vect.shape == (3,)
    assert vect.check_shape(Vector([2, 4, 6]))
    assert not vect.check_shape(Vector([1, 3]))


@raises(TypeError)
def test_vector_bad_shape():
    Vector([0, 0, [0, 0, 0], 0, 0])


@raises(TypeError)
def test_zeroes_bad_shape():
    Vector.zeroes([[11, 2], 3])


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
        self.int += 1
        return self.int


def test_random():
    length = 5
    assert Vector.random(length, 0, 10, Zeroes()) == Vector.zeroes(length)
    assert Vector.random(length, 0, 10, Ones()) == Vector([1] * length)
    assert Vector.random(length, 0, 10, Count()) == Vector([1, 2, 3, 4, 5])


def test_vector_add():
    assert Vector([1, 3, 3]) + Vector([1, 2, 3]) == Vector([2, 5, 6])
    assert Vector([1, 3, 3]) - Vector([1, 2, 3]) == Vector([0, 1, 0])


@raises(ShapeException)
def test_bad_add():
    Vector([1, 2, 3]) + Vector([1, 2])


def test_scalar_mult():
    assert Vector([1, 1, 1]) * 5 == Vector([5, 5, 5])


def test_dot():
    Vector([1, 3, 5]).dot(Vector([3, 1, 5])) == 16

if __name__ == '__main__':
    nose.main()
