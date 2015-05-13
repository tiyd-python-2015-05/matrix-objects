class Matrix():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()


    def shape(self):
        try:
            return (len(self.my_list), len(self.my_list[0]))
        except (TypeError,IndexError):
            raise ValueError('Not a 2d matrix')

class Vector():
    def __init__(self, my_list):
        self.my_list = my_list
        self.my_shape = self.shape()

    def shape(self):
        try:
            if len(self.my_list[0]) > 1:
                raise ValueError('Not a 1d vector')
        except TypeError:
            return (len(self.my_list),)
        except:
            raise ValueError('Not a 1d vector')
