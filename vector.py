import random
import math


class ShapeException(Exception):
    pass


class Vector:

    def __init__(self, arg):

        if type(arg) != type([]):
            raise ShapeException

        for item in arg:
            if not (type(item) == type(1) or type(item) == type(2.0)):
                raise TypeError("List items not integers or floats")

        self.values = arg
        self.shape = (len(arg),)

    @classmethod
    def zeroes(cls, length):
        """
        makes a zero vector of the given length
        """
        if type(length) != type(1):
            raise TypeError("input length is not an integer")

        return cls([0] * length)

    @classmethod
    def random(cls, length, start, end, random=random.Random()):
        """
        makes a vector of the given length
        with entries from random.randint(start, end)
        """
        if type(length) != type(1) or \
                type(start) != type(1) or \
                type(end) != type(1):

            raise ValueError

        return cls([random.randint(start, end) for _ in range(length)])

    def check_shape(self, other):
        """
        checks if the shapes match between
        the vector and other
        """
        return self.shape == other.shape

    def __add__(self, other):
        if self.check_shape(other):
            return Vector([entry1 + entry2 for entry1, entry2
                           in zip(self.values, other.values)])

        raise ShapeException

    def __mul__(self, other):
        if type(other) == type(1) or type(other) == type(2.0):
            return self.scalar_mult(other)

        else:
            raise ValueError("Cannot multiply {} and {}".format(type(self),
                                                                type(other)))

    def scalar_mult(self, other):
        """
        multiplies the vector by a scalar
        and returns the result
        """
        return Vector([val * other for val in self.values])

    def __eq__(self, other):
        return (type(self) == type(other) and
                self.shape == other. shape and
                self.values == other.values)

    def dot(self, other):
        if self.check_shape(other):
            return sum([coeff1 * coeff2 for (coeff1, coeff2)
                        in list(zip(self.values, other.values))])

        raise ShapeException

    @property
    def magnitude(self):
        """
        calculates the magnitude of the vector
        in the Euclidean norm
        """
        return math.sqrt(dot(self, self))

    def __str__(self):
        return "[" + ", ".join([str(val) for val in self.values]) + "]"

    def __repr__(self):
        return self.__str__()
