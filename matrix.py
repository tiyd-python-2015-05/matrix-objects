from vector import Vector, ShapeException

import random


class Matrix:

    def __init__(self, vectors, shape=None):
        if vectors:
            self.vectors = self.check_vectors(vectors)
            self.shape = (len(vectors), len(vectors[0]))

        else:
            if shape:
                self.shape = check_shape(shape)
                return Matrix.zeroes(shape)

    @classmethod
    def generate(cls, shape, gen_func):
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
    def random(cls, shape, start=0, end=10, random = random.Random()):
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
            vectors.append([random.randint(start,end) for _ in range(shape[1])])

        return cls(vectors)


    def check_vectors(self, vectors):
        """
        if possible calculates the shape
        of the matrix from the input vectors
        else raises ShapeException
        """
        x_len = len(vectors)
        vect_type = [item for item in vectors if type(item) == type(Vector)]
        list_type = [item for item in vectors if type(item) == type([])]
        try:
            if list_type:
                lengths = [len(item) for item in vectors]

                for item in lengths:
                    if item != lengths[0]:
                        raise ShapeException("unsuitable vectors used")

                return [Vector(item) for item in vectors]

            if vect_type:
                shapes = [time.shape for item in vectors]

                for item in shapes:
                    if item != shapes[0]:
                        raise ShapeException("unsuitable vectors used")

                return vectors

        except ShapeException:
            raise

        except Exceptions:

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
            type_check = type_check and type(entry) == type(1)

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
        if type(other) == type(int) or type(other) == type(2.0):
            return self.scalar_mult(other)

        if type(other) == type(Vector([1])):
            try:
                return self.vector_mult(other)
            except ShapeException:
                raise

        if type(other) == type(self):
            try:
                return self.matrix_mult(other)
            except ShapeException:
                raise

    @property
    def transpose(self):
        return Matrix([[row.values[i] for row in self.vectors]
                        for i in range(self.shape[1])])

    def scalar_mult(self, other):
        return Matrix([vector * other for vector in self.vectors])

    def vector_mult(self, other):
        return Vector([vector.dot(other) for vector in self.vectors])

    def matrix_mult(self, other):
        if self.shape == other.shape:
            return Matrix([[vect1.dot(vect2) for vect2 in
                            other.transpose.vectors]
                            for vect1 in self.vectors])

        raise ShapeException


    def __pow__(self, other):
        if type(other) != type(1):
            raise TypeError("power must be an integer")

        if other < 1:
            raise TypeError("power must be positive")

        # insert recursive multiply here

    def __add__(self, other):
        try:
            if self.shape == other.shape:
                return [row1 + row2 in zip(self.vectors, other.vectors)]

        except Exception:
            raise

    def __str__(self):
        return "\n".join([vector.__str__() for vector in self.vectors])

    def __repr__(self):
        return self.__str__()
