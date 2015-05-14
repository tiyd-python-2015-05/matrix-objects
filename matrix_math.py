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



class Matrix:
    def __init__(self, rows):
        self.rows = rows

    @property
    def shape(self):
        return (len(self.rows), len(self.rows[0]))


    def __repr__(self):
        return ("Matrix: {}".format(self.rows))


    def __eq__(self, other):
        if isinstance(other, list):
            return self.rows == other
        return self.rows[0] == other.rows[0]


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
        #    matr = ([[Vector(self.rows[i]).dot(other.matrix_col(j)) for j in
        #            range(other.matrix_col(0).shape[0])] for i in range(len(self.rows))])
            matr = ([[(Vector(self.rows[i])).dot(other.matrix_col(j)) for j in
                        range(len(self.rows))] for i in range(len(other.rows[0]))])

            #other.matrix_col(0)).row
        #    matr = ([[Vector(self.rows[i]).dot(other.matrix_col(j)) for j in Vector(self.rows[i])] for j in (other.matrix_col(j))])
            return Matrix(matr)
        #    return [[dot(a[i],matrix_col(b, j)) for j in range(len(b[0]))] for i in range(len(a))]


    """
    [[a b]   *  [[w x]   =   [[a*w+b*y a*x+b*z]
     [c d]       [y z]]       [c*w+d*y c*x+d*z]
     [e f]                    [e*w+f*y e*x+f*z]]

    Matrix * Matrix = Matrix
    """


    def matrix_col(self, column):
        col = [i[column] for i in self.rows]
        return Vector(col)
    """
    [[a b]   *  [x   =   [a*x+b*y
     [c d]       y]       c*x+d*y
     [e f]                e*x+f*y]

    Matrix * Vector = Vector
    """

#
# shape
# addition and subtraction
# multiplication by a scalar
# matrix multiplication by a vector
# matrix multiplication by a matrix
# vector dot product
# vector magnitude

if __name__ == "__main__":
    drake_matrix = Matrix([[0.00, 0.25, 0.60, 0.80, 0.15, 0.00],
                           [0.70, 0.00, 0.00, 0.00, 0.00, 0.00],
                           [0.00, 0.95, 0.00, 0.00, 0.00, 0.00],
                           [0.00, 0.00, 0.90, 0.00, 0.00, 0.00],
                           [0.00, 0.00, 0.00, 0.90, 0.00, 0.00],
                           [0.00, 0.00, 0.00, 0.00, 0.50, 0.00]])

    population_vector = Vector([10, 0, 0, 0, 0, 0])

    for i in range(10):
        population_vector = drake_matrix * population_vector
        print("After {} years, the population vector is {}".format((i*2+2),
                population_vector))
