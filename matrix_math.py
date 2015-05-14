


class Vector:
    def __init__(self, vector):
        self.vector = vector


    def shape(self):
        try:
         return (len(self.vector), len(self.vector[0]))
     except TypeError:
         return (len(self.vector),)

    def vector_add(self):
        if shape(self.vector1) != shape(vector2):
            raise ShapeException()
        return [vector1[i] + vector2[i] for i in range(len(a))]

    def vector_sub(self):
        if shape(a) != shape(b):
            raise ShapeException()
        return [a[i] - b[i] for i in range(len(a))]

    def vector_mult_by_scaler









class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
