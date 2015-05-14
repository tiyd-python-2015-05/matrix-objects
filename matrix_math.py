import math
from numbers import Number

class ShapeException(Exception):
    pass

class Vector:
    def __init__(self, row):
        self.row = row

    @property
    def shape(self):
        return len(self.row),

    def __repr__(self):
        return ("Vector: {}".format(self.row))

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
        if isinstance(other, Number):
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
        if self.shape != other.shape:
            raise ShapeException("Vectors must be same shape.")
        return sum([self.row[i] * other.row[i] for i in range(len(self.row))])

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
        return (len(self.rows), len(self.rows[0]))



    #
    # def __eq__(self, other):
    #


#isinstance(other, Number)

    def __eq__(self, other):
        if isinstance(other, list):
            return self.rows == other
        return self.rows == other.rows

    def __mul__(self, other):
        if isinstance(other, Number):
            mult_matr = [(Vector(self.rows[i]) * other) for i in range(len(self.rows))]
            return Matrix(mult_matr)
        elif isinstance(other, Vector):
#            if self.shape[0] != other.shape:
#                raise ShapeException("Columns of matrix not equal vector shape")
            vec = ([Vector(self.rows[i]).dot(other) for i in range(len(self.rows))])
            return Vector(vec)
        elif isinstance(other, Matrix):
#            mult_matr =
#            return Matrix(mult_matr)
            pass

    def matrix_col(self, column):
        col = [i[column] for i in self.rows]
        return Vector(col)
    """
    [[a b]   *  [x   =   [a*x+b*y
     [c d]       y]       c*x+d*y
     [e f]                e*x+f*y]

    Matrix * Vector = Vector
    """

    # matrix_matrix_multiply_checks_shapes(matrix1, matrix2)
    # mult_matrix = [matrix_col(matrix2, i) for i in range(len(matrix2[0]))]
    # row_len = len(mult_matrix)
    # list1 = [dot((matrix1[i]), (mult_matrix[j])) for i in range(len(matrix1)) for \
    #         j in range(len(mult_matrix))]
    # return [list1[i:i + row_len] for i in range(0, len(list1), row_len)]
    #
#
# shape
# addition and subtraction
# multiplication by a scalar
# matrix multiplication by a vector
# matrix multiplication by a matrix
# vector dot product
# vector magnitude
