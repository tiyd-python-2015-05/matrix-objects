import math

class Vector:
    def __init__(self, vector):
        self.vector = vector


    def shape(self):
        if isinstance(self.vector[0], int):
            return (len(self.vector), )


    def __eq__(self, other):
        return len(self.vector) == len(other.vector)


    def __add__(self, other):
        if self != other:
            raise TypeError("Cannot add vector {} to vector {}.".format(
                             other, self.vector))
        else:
            return [x + y for x, y in zip(self.vector, other.vector)]


    def __sub__(self, other):
        if self != other:
            raise TypeError("Cannot subtract vector {} from vector {}.".format(
                             other, self.vector))
        else:
            return [x - y for x, y in zip(self.vector, other.vector)]


    def __mul__(self, scalar):
        return [self.vector[i] * scalar for i in range(len(self.vector))]


    def vector_dot(self, other):
        if self != other:
            raise TypeError
        else:
            return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])


    def magnitude(self):
        return math.sqrt(sum([self.vector[i]**2 for i in range(len(self.vector))]))



class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def shape(self):
        if isinstance(self.matrix[0], list):
            return (len(self.matrix), len(self.matrix[1]))


    def __eq__(self, other):
        return len(self.matrix) == len(other.matrix[0])


    def __add__(self, other):
        if self != other:
            raise TypeError("Cannot add matrix {} to matrix {}.".format(
                             other.matrix, self.matrix))
        else:
            return [Vector(self.matrix[x]) + Vector(other.matrix[x])
                    for x in range(len(self.matrix))]


    def __mul__(self,other):
        if isinstance(other, int):
            return [Vector(i) * other for i in self.matrix]
        elif isinstance(other, Vector):
            return
        elif isinstance(other, Matrix):
            return


    def transpose(self):
        return [self.matrix[len(self.matrix) - j - 1][i]
                for i, j in range(len(self.matrix))]
