
class ShapeException(Exception):
    pass


class Vector:
    def __init__(self, vector):
        self.vector = vector



    def shape(self):
        try:
            return (len(self.vector), len(self.vector[0]))
        except TypeError:
            return (len(self.vector), )


    def vector_add(self, other):
        if Vector.shape(self.vector) != Vector.shape(other.vector):
            raise ShapeException()
        return [self.vector[i] + other.vector[i] for i in range(len(self.vector))]


    def vector_sub(self, other):
        if shape(self.vector) != shape(self.other):
            raise ShapeException()
        return [self.vector[i] - other.vector[i] for i in range(len(self.vector))]


    def vector_mult_by_scaler(self, scaler):
        return [self.vector[i] * scalar for i in range(len(self.vector))]


    def vector_dot(self, other):
        if shape(self.vector) != shape(other.vector):
            raise ShapeException()
        return [self.vector[i] * other.vector[i] for i in range(len(self.vector))]


    def vector_mag(self):
        return math.sqrt(sum(self.vector[i]**2 for i in range(len(self.vector))))






# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix
#
#     def shape(self):
#
#     def matrix_add(self, other):
#
#     def matrix_subtract(self, other):
#
#     def matrix_mult_scaler(self, scaler):
#         return [[value * scaler for value in row] for row in matrix]
#
#
#     def matrix_mult_vector(self, vector):
#
#     def matrix_mult(self, other):
