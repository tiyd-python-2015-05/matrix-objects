import math
class ShapeException(Exception):
    pass

class Vector:
    def __init__(self, a_list):
        self.contents = a_list

    def shape(self):
        return (len(self.contents),)

    def __eq__(self,other):
        if type(other) == Vector:
            return self.contents == other.contents
        elif type(other) == list:
            return self.contents == other
        else:
            raise TypeError("Can't compare those values")

    def __str__(self):
        return str(self.contents)

    def __add__(self, other):
        a = self.contents
        b = other.contents
        if self.shape() != other.shape():
            raise ShapeException()
        return [a[i] + b[i] for i in range(len(a))]

    def __sub__(self, other):
        a = self.contents
        b = other.contents
        if self.shape() != other.shape():
            raise ShapeException()
        return [a[i] - b[i] for i in range(len(a))]

    def dot(self, other):
        a = self.contents
        b = other.contents
        if self.shape() != other.shape():
            raise ShapeException()
        return sum([(a[i] * b[i]) for i in range(len(a))])

    def __mul__(self, scalar):
        a = self.contents
        return [a[i] * scalar for i in range(len(a))]

    def magnitude(self):
        a = self.contents
        return math.sqrt(sum([a[i]**2 for i in range(len(a))]))


class Matrix:
    def __init__(self, some_lists):
        self.contents = some_lists

    def __eq__(self,other):
        if type(other) == Matrix:
            return self.contents == other.contents
        elif type(other) == list:
            return self.contents == other
        else:
            raise TypeError("Can't compare those values")

    def __repr__(self):
        return str(self.contents)

    def shape(self):
        a = self.contents
        return (len(a),len(a[1]))

    def __add__(self, other):
        a = self.contents
        b = other.contents
        if self.shape() != other.shape():
            raise ShapeException()
        return [Vector(a[i]) + Vector(b[i]) for i in range(len(a))]

    def __sub__(self, other):
        a = self.contents
        b = other.contents
        if self.shape() != other.shape():
            raise ShapeException()
        return [Vector(a[i]) - Vector(b[i]) for i in range(len(a))]

    def matrix_col(self, column_index):
        a = self.contents
        return [l[column_index] for l in a]

    def __mul__(self,other):
        if type(other) == Vector:
            if len(other.contents) != len(self.contents[1]):
                raise ShapeException()
            return[Vector.dot(Vector(self.contents[i]), other) for i in range(len(self.contents))]
        elif type(other) == Matrix:
            a = self.contents
            b = other.contents
            if len(a[0]) != len(b):
                raise ShapeException()
            return [[Vector.dot(Vector(a[i]),Vector([l[j] for l in b])) for j in range(len(b[0]))] for i in range(len(a))]
        elif type(other) == int:
            a = self.contents
            return[Vector(i) * other for i in a]
        else:
            raise TypeError("Cannot multiply these values")

    def rotate_matrix(self):
        a = self.contents
        rot_mat = []
        for i in range(len(a[0])):
            j = self.matrix_col(i)
            new_row = j[::-1]
            rot_mat.append(new_row)
        return Matrix(rot_mat)

    @classmethod
    def newMat(cls, size):
        matrix = []
        for i in range(size):
            matrix.append([0,0,0])
        return cls(matrix)


def find_population(l, d):
    num_of_cycles = 20
    product = Vector(l * d)
    while num_of_cycles > 0:
        new_prod = l * product
        product = Vector(new_prod)
        num_of_cycles -= 1
    return product

Leslie_mat = Matrix([[0, 0.25, 0.6, 0.8, 0.15, 0], [0.7, 0, 0, 0, 0, 0], [0, 0.95, 0, 0, 0, 0],
                    [0, 0, 0.9, 0, 0, 0], [0, 0, 0, 0.9, 0, 0], [0, 0, 0, 0, 0.5, 0]])

initial_group = Vector([10, 0, 0, 0, 0, 0])

print(find_population(Leslie_mat, initial_group))
