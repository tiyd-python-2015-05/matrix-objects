

class Vector:
    def __init__(self, vec1):
        self.vec1=vec1

    def shape_of(self):
        return (len(self.vec1), )


    def __eq__(self, other):
        return self.vec1 == other.vec1


    def __add__(self, other):
        # if shape_of(self.vec1) != shape_of(self.vec1):
        #     raise ShapeException("That ain't gonna work")
        return Vector([self.vec1[i]+other.vec1[i] for i in range(len(self.vec1))])


    def __sub__(self,other):
        return Vector([self.vec1[i]-other.vec1[i] for i in range(len(self.vec1))])

    def __mul__(self,other):
        return Vector([self.vec1[i] * other for i in range(len(self.vec1))])


class Matrix:
    def __init__(self,mat1):
        self.mat1 = mat1
    
