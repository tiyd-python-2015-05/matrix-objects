class ShapeException(Exception):
    pass

class Vector():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()
    def __add__(self, other):
        if self.shape() != other.shape():
            raise ShapeException
        return Vector([self.my_list[i] + other.my_list[i] for i in range(self.shape()[0])])

    def __sub__(self, other):
        other = other * -1
        return self + other
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector([i * other for i in self.my_list])
        else:
            return None
    def __eq__(self, other):
        return self.my_list == other.my_list

    def shape(self):
        try:
            if len(self.my_list[0]) > 1:
                raise ValueError('Not a 1d vector')
        except TypeError:
            return (len(self.my_list),)
        except:
            raise ValueError('Not a 1d vector')
    def dot(self, other):
        pass
        
class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()


    def shape(self):
        try:
            return (len(self.my_list), len(self.my_list[0]))
        except (TypeError,IndexError):
            raise ValueError('Not a 2d matrix')
