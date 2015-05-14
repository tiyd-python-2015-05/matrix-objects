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

    def __eq__(self, other):
        if isinstance(other, list):
            return self.row == other
        else:
            return self.row == other.row

    def __add__(self, other):
        if self.shape != other.shape:
            raise ShapeException("Vector must be same shape.")
        row_add = [self.row[i] + other.row[i] for i in range(len(self.row))]
        return Vector(row_add)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ShapeException("Vector must be same shape.")
        row_sub = [self.row[i] - other.row[i] for i in range(len(self.row))]
        return Vector(row_sub)

    def __mul__(self, other):
        if isinstance(other, Number):
            row_mul_scal = [self.row[i] * other for i in range(len(self.row))]
            return Vector(row_mul_scal)
        # 
        # elif isinstance(other, Vector):
        #     vec_mul_vec = [self.row[i] * other.row[i] for i in range(len(self.row))]
        #     return Vector(vec_mul_vec) #is this needed? Or can just return func
        else:
            raise ShapeException("Vector must be * by a scalar or Vector.")

    # def __repr__(self):
    #     return "Vector: {}".format(self.row)

    def magnitude(self):
        return math.sqrt(sum([num * num for num in self.row]))

    def dot(self, other):
        """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
        if self.shape != other.shape:
            raise ShapeException("Vector must be same shape.")
        #return sum([self.row[i] * other.row[i] for i in range(len(self.row))])
        return sum([x * y for x, y in zip(self.row, other.row)])

class Matrix:
    def __init__(self, rows):
        self.rows = rows

    @property
    def shape(self):
        return len(self.rows), len(self.rows[0])

    def __eq__(self, other):
        if isinstance(other, list):
            return self.rows == other
        else:
            return self.rows == other.rows

    def __mul__(self, other):
        if isinstance(other, Number):
            rows_mul_scal = [Vector(self.rows[i]) * other for i in range(len(self.rows))]
            return Matrix(rows_mul_scal)

        elif isinstance(other, Matrix):
            rows_mul_rows = [self.matrix_col(i) * Vector(self.rows[i]) for i in range(len(self.rows))]
            return Matrix(rows_mul_rows)

        else:
            raise ShapeException("Matrix must be * by scalar.")

    def matrix_col(self, column):
        col = [i[column] for i in self.rows]
        return Vector(col)

    # return [[sum(a*b for a,b in zip(matrix1_row, matrix2_col)) \
    # for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    #
    # return [[dot(a[i],matrix_col(b, j)) for j in range(len(b[0]))] for i in range(len(a))]
