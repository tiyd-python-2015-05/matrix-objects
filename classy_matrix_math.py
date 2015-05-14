class ShapeException(Exception):
    pass

class Vector:

    def __init__(self, alist):
        self.alist = alist

    def __eq__(self, other):
        return self.alist == other.alist

    def shape(self):
        return (len(self.alist), )

    def __repr__(self):
        return "Vector({})".format(self.alist)

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Vector([self.alist[idx] + other.alist[idx] for idx \
                                in range(len(self.alist))])

    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Vector([self.alist[idx] - other.alist[idx] for idx \
                                in range(len(self.alist))])

    def __mul__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Vector([self.alist[idx] * other.alist[idx] for idx \
                                in range(len(self.alist))])

    def dot(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return sum([num for num in (self * other).alist])

    def vector_multiply(self, other):
        return [num * other for num in self.alist]

class Matrix:

    def __init__(self, alist):
        self.alist = alist

    def __eq__(self, other):
        return self.alist == other.alist

    def matrix_shape(self):
        for vec in self.alist:
            if len(vec) == len(self.alist[0]):
                return (len(self.alist), len(self.alist[len(self.alist)-1]))

    def matrix_row(self, row_number):
        return self.alist[row_number]
