import matplotlib.pyplot as plt

from random import choice

class RandomWalk():
    """A class to generate random walks"""
    def __init__(self,num_points=5000):
        #Anitialize attributes of walk.
        self.num_points = num_points

        #all walk start at (0, 0).
        self.x_value = [0]
        self.y_value = [0]


    def fill_walk(self):
        """calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_value) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)

# hk = RandomWalk(40)
# hk.fill_walk()
#
# plt.scatter(hk.x_value, hk.y_value, s=20)
# plt.show()



