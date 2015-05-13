import math

class ShapeException(Exception):
    pass

class Vector:
    def __init__(self, values):
        self.values = self.is_vector(values)
        self.shape = len(self.values),

    def __eq__(self, other):
        return self.values == other.values

    def __add__(self, other):
        if self.shape != other.shape:
            raise ShapeException()
        else:
            return Vector([self.values[index] + other.values[index]
                           for index in range(len(self.values))])

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ShapeException()

        else:
            return Vector([self.values[index] - other.values[index]
                           for index in range(len(self.values))])

    def __mul__(self, other):
        return Vector([self.values[index] * other
                       for index in range(len(self.values))])

    def dot(self, other):
        if self.shape != other.shape:
            raise ShapeException()
        else:
            return sum([self.values[index] * other.values[index]
                        for index in range(len(self.values))])

    def mag(self):
        return math.sqrt(sum([coefficient ** 2
                    for coefficient in self.values]))

    def is_vector(self, a_list):
            if type(a_list) != list:
                raise ValueError(
                "Must make Vector with numerical list")
            else:
                for item in a_list:
                    if not isinstance(item, (int, float)):
                        raise ValueError(
                        "Must make Vector with numerical list")
                return a_list


###############################################################################


class Matrix:
    def __init__(self, values):
        self.values = self.is_matrix(values)
        self.shape = len(self.values),len(self.values[0])

    def __eq__(self, other):
        return self.values == other.values

    def __add__(self, other):
        if self.shape != other.shape:
            raise ShapeException()
        else:
            return Matrix([[self.values[row][index] + other.values[row][index]
                           for index in range(len(self.values[0]))]
                           for row in range(len(self.values))])

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ShapeException()
        else:
            return Matrix([[self.values[row][index] - other.values[row][index]
                           for index in range(len(self.values[0]))]
                           for row in range(len(self.values))])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.values[row][index] * other
                            for index in range(len(self.values[0]))]
                            for row in range(len(self.values))])

        elif isinstance(other, Vector):
            return Vector([other.dot(Vector(row)) for row in self.values])

        elif isinstance(other, Matrix):
            return Matrix([(other.transpose() * Vector(row)).values
                          for row in self.values])

    def transpose(self):
        return Matrix([[row[index]
                        for row in self.values]
                        for index in range(len(self.values[0]))])

    def is_matrix(self, a_list):
        if type(a_list) != list:
            raise ValueError(
            "Must make Matrix with list of numerical lists")
        else:
            for index in range(len(a_list)):
                if type(a_list[index]) != list or \
                 len(a_list[index]) != len(a_list[(index-1)]):
                    raise ValueError(
                    "Must make Matrix with list of numerical lists")
                else:
                    for value in a_list[index]:
                        if not isinstance(value, (int, float)):
                            raise ValueError(
                        "Must make Matrix with list of numerical lists")
        return a_list

    @classmethod
    def from_function(cls, rows, columns, function):
        return cls([[function(x, y) for y in range(columns)]
                     for x in range(rows)])
