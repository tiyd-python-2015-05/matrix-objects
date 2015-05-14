class ShapeException(Exception):
    pass


class Vector():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Vector([self.my_list[i] + other.my_list[i]
                       for i in range(self.shape()[0])])

    def __sub__(self, other):
        other = other * -1
        return self + other

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector([i * other for i in self.my_list])
        else:
            raise ValueError('Vector can only be multiplied by \
                              scalar (int/float)')

    def __eq__(self, other):
        return self.my_list == other.my_list

    def __repr__(self):
        return 'Vector({})'.format(self.my_list)

    def shape(self):
        try:
            if len(self.my_list[0]) > 1:
                raise ValueError('Not a 1d vector')
        except TypeError:
            return (len(self.my_list),)
        except:
            raise ValueError('Not a 1d vector')

    def dot(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return sum([self.my_list[i] * other.my_list[i]
                    for i in range(len(self.my_list))])

    def magnitude(self):
        return self.dot(self)**0.5


class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()

    @classmethod
    def create(cls, size=(2, 2), fn = lambda x, y: 1):
        return Matrix([[fn(i, j) for j in range(size[0])]
                       for i in range(size[1])])

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Matrix([self.my_list[i] + other.my_list[i]
                       for i in range(self.shape()[0])])

    def __sub__(self, other):
        other = other * -1
        return self + other

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[i * other for i in row] for row in self.my_list])

        elif type(other) is Vector:
            if self.shape()[1] != other.shape()[0]:
                raise ShapeException

            step1 = [[val * other.my_list[idx] for idx, val in enumerate(row)]
                     for row in self.my_list]
            return Vector([sum(x) for x in step1])

        elif type(other) is Matrix:
            if self.shape()[1] != other.shape()[0]:
                raise ShapeException

            y_transposed = [[row[i] for row in other.my_list]
                            for i in range(len(other.my_list[0]))]

            return Matrix([[Vector(row).dot(Vector(col))
                            for col in y_transposed] for row in self.my_list])

        else:
            raise ValueError('Matrix can only be multiplied by '
                               'scalar, Vector, or Matrix')

    def __eq__(self, other):
        return self.my_list == other.my_list

    def __repr__(self):
        return 'Matrix({})'.format(self.my_list)

    def shape(self):
        try:
            return (len(self.my_list), len(self.my_list[0]))
        except (TypeError, IndexError):
            raise ValueError('Not a 2d matrix')

    def rotate(self):
        tuple_list = list(zip(*self.my_list[::-1]))
        return Matrix([list(row) for row in tuple_list])
