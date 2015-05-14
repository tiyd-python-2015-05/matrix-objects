import random
import math
from number import Number


class ShapeException(Exception):
    pass


class Vector:

    def __init__(self, arg):

        if not isinstance(arg, list):
            raise ShapeException

        for item in arg:
            if not (isinstance(item, Number)):
                raise TypeError("List items not ints or floats")

        self.values = tuple(arg)
        self.shape = (len(arg),)

    @classmethod
    def zeroes(cls, length):
        """
        makes a zero vector of the given length
        """
        if not isinstance(length, int):
            raise TypeError("input length is not an int")

        return cls([0] * length)

    @classmethod
    def random(cls, length, start, end, random=random.Random()):
        """
        makes a vector of the given length
        with entries from random.randint(start, end)
        """
        if not (isinstance(length, int) or
                isinstance(start, int) or
                isinstance(end, int)):

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

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
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
        in the E
        """
        return math.sqrt(self.dot(self))

    def __str__(self):
        return "[" + ", ".join([str(round(val, 3))
                                for val in self.values]) + "]"

    def __repr__(self):
        return self.__str__()
