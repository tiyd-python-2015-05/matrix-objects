import math

class ShapeException(Exception):
    pass

class Vector:
    def __init__(self, row):
        self.row = row

    @property
    def shape(self):
        return len(self.row),


    def __eq__(self, other):
        if isinstance(other, list):
            return self.row == other
        else:
            return self.row == other.row

    def __add__(self, other):
        if self.shape != other.shape:
            raise ShapeException("Vectors must be same shape.")
        sum_vec = ([self.row[i] + other.row[i] for i in range(len(self.row))])
        return Vector(sum_vec)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ShapeException("Vectors must be same shape.")
        sub_vec = ([self.row[i] - other.row[i] for i in range(len(self.row))])
        return Vector(sub_vec)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            mul_vec = ([other * self.row[i] for i in range(len(self.row))])
            return Vector(mul_vec)
        else:
            raise ShapeException("Vectors can only be multiplied by scalar")

    def magnitude(self):
        """
        magnitude([a b])  = sqrt(a^2 + b^2)

        magnitude(Vector) = Scalar
        """
        return math.sqrt(sum([num * num for num in self.row]))

    def dot(self, other):
        pass

    # def vector_sum(*vectors):
    #     """vector_sum can take any number of vectors and add them together."""
    #     vector_sum_checks_shapes(vectors)
    #     sum = vectors[0]
    #     for vec in vectors[1:]:
    #         sum = vector_add(sum, vec)
    #     return sum

    # def __eq__(self, other):
    #     if isinstance(other, list):
    #         return self.row == other
    #     else:
    #         return self.row == other.row

    # def shape_vectors(self):
    #
    #     if isinstance(self, Vector):
    #         return (len(self.row),)
    #     elif isinstance(self, Matrix):
    #         return (len(self.rows), len((self.rows)[0]))
    #     else:
    #         pass





class Matrix:
    def __init__(self, rows):
        self.rows = rows

    @property
    def shape(self):
        return (len(self.rows[0]), len(self.rows))


#
# shape
# addition and subtraction
# multiplication by a scalar
# matrix multiplication by a vector
# matrix multiplication by a matrix
# vector dot product
# vector magnitude
