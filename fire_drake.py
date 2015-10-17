from matrix import Matrix
from vector import Vector

current_drakes = Vector([10, 0, 0, 0, 0, 0])

leslie = Matrix([[0, .25, .6, .8, .15, 0],
                 [.7, 0, 0, 0, 0, 0],
                 [0, .95, 0, 0, 0, 0],
                 [0, 0, .9, 0, 0, 0],
                 [0, 0, 0, .9, 0, 0],
                 [0, 0, 0, 0, .5, 0]])


drakes_future = leslie ** 20 * current_drakes
print(drakes_future)
