import matplotlib.pyplot as plt

from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    #make a random walk, and plot the point.
    hk = RandomWalk(2000000)
    hk.fill_walk()
    pointNumber = list(range(hk.num_points))
    plt.scatter(hk.x_value,hk.y_value, c=pointNumber, cmap=plt.cm.Blues, edgecolors='none', s=2)

    #Emphasize the first and last points.
    plt.scatter(0, 0, c='green',edgecolors='none',s=100)
    plt.scatter(hk.x_value[-1], hk.y_value[-1],c='red', edgecolors='none',s=100)

    #remove axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keepRunning = input("Make anotherbwalk?(y/n):")
    if keepRunning == 'n':
        break

