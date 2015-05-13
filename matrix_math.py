import math
class ShapeException(Exception):
    pass


def vector_add(a,b):
    if shape(a) != shape(b):
        raise ShapeException()
    return [a[i] + b[i] for i in range(len(a))]


def vector_sub(a,b):
    if shape(a) != shape(b):
        raise ShapeException()
    return [a[i] - b[i] for i in range(len(a))]


def vector_sum(*vectors):
    size = len(vectors[1])
    for v in vectors:
        if len(v) != size:
            raise ShapeException()
    return [sum(i) for i in zip(*vectors)]


def dot(a, b):
    if shape(a) != shape(b):
        raise ShapeException()
    return sum([(a[i] * b[i]) for i in range(len(a))])


def vector_multiply(a, scalar):
    return [a[i] * scalar for i in range(len(a))]


def vector_mean(*vectors):
    return [sum(i)/len(i) for i in zip(*vectors)]


def magnitude(a):
    return math.sqrt(sum([a[i]**2 for i in range(len(a))]))


def shape(a):
    if type(a[0]) == int:
        return (len(a),)
    else:
        return (len(a),len(a[1]))


def matrix_row(a, row):
    return a[row]


def matrix_col(a, column):
    return [l[column] for l in a]


def matrix_scalar_multiply(a, scalar):
    return[vector_multiply(i,scalar) for i in a]


def matrix_vector_multiply(matrix,vector):
    if len(vector) != len(matrix[1]):
        raise ShapeException()
    return[dot(matrix[i], vector) for i in range(len(matrix))]


def matrix_matrix_multiply(a,b):
    if len(a[0]) != len(b):
        raise ShapeException()
    return [[dot(a[i],matrix_col(b, j)) for j in range(len(b[0]))] for i in range(len(a))]
