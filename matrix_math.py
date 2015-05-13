

def shape_vectors(item):
    if isinstance(item, Vector):
        return (len(item.row),)
    elif isinstance(item, Matrix):
        return (len((item.rows)[0]), len(item.rows))
    else:
        pass

class ShapeException(Exception):
    pass

class Vector:
    def __init__(self, row):
        self.row = row

    def __add__(self, other):
        if shape_vectors(self) != shape_vectors(other):
            raise ShapeException("Vectors must be same shape.")

        return [self.row[i] + other.row[i] for i in range(len(self.row))]

    def __eq__(self, other):
        if isinstance(other, list):
            return self.row == other
        else:
            return self.row == other.row

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

#
# shape
# addition and subtraction
# multiplication by a scalar
# matrix multiplication by a vector
# matrix multiplication by a matrix
# vector dot product
# vector magnitude
