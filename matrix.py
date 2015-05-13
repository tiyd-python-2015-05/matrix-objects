from vector import Vector

import random


class ShapeException(Exception):
    pass


class Matrix:

    def __init__(self, vectors, shape=None):
        if vectors:
            self.shape = self.check_vectors(vectors)
            self.values = vectors

        else:
            if shape:
                self.shape = check_shape(shape)
                return Matrix.zeroes(shape)

    @classmethod
    def zeroes(cls, shape):
        """
        Generates a matrix of zeroes with the given shape
        """
        cls.check_shape(cls, shape)
        values = []

        for y_val in range(shape[0]):
            values.append(Vector.zeroes(shape[1]))

        return cls(values)

    @classmethod
    def random(cls, shape, random = random.Random(), start=0, end=10):
        """
        takes a random number generator
        and fills a matrix of a given shape
        with random numbers
        """
        values = []
        try:
            cls.check_shape(cls, shape)
        except ShapeException:
            raise


        for y_len in range(shape[0]):
            values.append(Vector.random(shape, random, start, end))

        return cls(vectors)


    def check_vectors(self, vectors):
        """
        if possible calculates the shape
        of the matrix from the input vectors
        else raises ShapeException
        """
        x_len = len(vectors)
        type_check_vect = True
        type_check_mat = True
        for item in vectors:
            type_check_vect = type_check_vect and type(item) == type(1)
            type_check_matrix = type_check_mat and type(item) == type([])

        if type_check_vect:
            return x_len, 0

        if type_check_mat:

            len_check_mat = True
            ref = len(vectors[0])

            for item in vectors:
                if len(item) != ref:
                    len_check_mat = False

            if len_check_mat:
                return x_len, ref

        raise ShapeException("Unsuitable vectors used")


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
            return self.shape == other.shape and self.values == other.values
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
