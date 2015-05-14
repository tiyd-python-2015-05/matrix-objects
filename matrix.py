from vector import Vector, ShapeException

import random


class Matrix:

    def __init__(self, vectors, shape=None):
        if vectors:
            self.vectors = self.check_vectors(vectors)
            self.shape = (len(vectors), self.vectors[0].shape[0])

        else:
            if shape:
                self.shape = self.check_shape(shape)
                return Matrix.zeroes(shape)

    @classmethod
    def generate(cls, shape, gen_func):
        """
        creates a matrix whose values
        are the result of calling gen_func
        """
        if cls.check_shape(cls, shape):
            return cls([[gen_func() for _ in range(shape[0])]
                        for _ in range(shape[1])])

        raise ShapeException

    @classmethod
    def zeroes(cls, shape):
        """
        Generates a matrix of zeroes with the given shape
        """
        cls.check_shape(cls, shape)
        values = []

        for y_val in range(shape[0]):
            values.append([0 for _ in range(shape[1])])

        return cls(values)

    @classmethod
    def random(cls, shape, start=0, end=10, random=random.Random()):
        """
        takes a random number generator
        and fills a matrix of a given shape
        with random numbers
        """
        vectors = []
        try:
            cls.check_shape(cls, shape)
        except ShapeException:
            raise

        for y_len in range(shape[0]):
            vectors.append([random.randint(start, end)
                            for _ in range(shape[1])])

        return cls(vectors)

    def check_vectors(self, vectors):
        """
        checks the input vectors
        to see if they are in fact
        lists or vectors, then checks
        their lengths.  If they are
        all the same length it returns
        a list of vectors
        """
        vect_type = [item for item in vectors if isinstance(item, Vector)]
        list_type = [item for item in vectors if isinstance(item, list)]
        none_type = [item for item in vectors
                     if item not in vect_type and item not in list_type]

        if none_type:
            raise TypeError("supplied vectors are of incorrect type")

        try:
            if list_type and not vect_type:
                lengths = [len(item) for item in vectors]

                for item in lengths:
                    if item != lengths[0]:
                        raise ShapeException("unsuitable vectors used")

                return [Vector(item) for item in vectors]

            if vect_type and not list_type:
                shapes = [item.shape for item in vectors]

                for item in shapes:
                    if item != shapes[0]:
                        raise ShapeException("unsuitable vectors used")

                return vectors

            raise TypeError("mismatched input types")

        except ShapeException:
            raise

        except Exception:

            return ValueError("bad initial vectors")

    def check_shape(self, shape):
        """
        tests whether shape is acceptable
        e.g. a single integer or
        two integers in a list/tuple
        """
        size_check = (len(shape) == 1 or len(shape) == 2)
        type_check = True
        for entry in shape:
            type_check = type_check and isinstance(entry, int)

        if not (size_check and type_check):
            raise ShapeException

        else:
            return True

    def __eq__(self, other):
        try:
            return self.shape == other.shape and self.vectors == other.vectors

        except Exception:
            raise

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.scalar_mult(other)

        if isinstance(other, Vector):
            try:
                return self.vector_mult(other)
            except ShapeException:
                raise

        if isinstance(other, Matrix):
            try:
                return self.matrix_mult(other)
            except ShapeException:
                raise

    @property
    def transpose(self):
        """
        the transpose of the matrix
        """
        return Matrix([[row.values[i] for row in self.vectors]
                       for i in range(self.shape[1])])

    def scalar_mult(self, other):
        """
        multiplies the matrix by a constant
        """
        return Matrix([vector * other for vector in self.vectors])

    def vector_mult(self, other):
        """
        multiplies a vector by self
        and returns the resulting vector
        """
        return Vector([vector.dot(other) for vector in self.vectors])

    def matrix_mult(self, other):
        """
        multiplies the matrix by a another matrix
        and returns the resulting matrix
        """
        if self.shape == other.shape:
            return Matrix([[vect1.dot(vect2) for vect2 in
                            other.transpose.vectors]
                           for vect1 in self.vectors])

        raise ShapeException

    def __pow__(self, other):
        if not isinstance(other, int):
            raise TypeError("power must be an integer")

        if other < 1:
            raise TypeError("power must be positive")

        return self.remult(other)

    def remult(self, num):
        """
        returns a matrix raised to a positive integer power
        """
        if num > 1:
            return self.remult(num - 1) * self
        else:
            return self

    def __add__(self, other):
        try:
            if self.shape == other.shape:
                return Matrix([row1 + row2 for row1, row2
                               in zip(self.vectors, other.vectors)])

        except Exception:
            raise

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __str__(self):
        return "\n".join([vector.__str__() for vector in self.vectors])

    def __repr__(self):
        return self.__str__()
