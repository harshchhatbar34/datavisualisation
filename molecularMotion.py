import matplotlib.pyplot as plt

from random_walk import RandomWalk
# Keep making new walks, as long as the program is active.
while True:
    #make a random walk, and plot the point.
    hk = RandomWalk(4)
    hk.fill_walk()
    #Set the size of thr plotting window.
    plt.figure(dpi=128 , figsize=(10, 6))

    pointNumber = list(range(hk.num_points))
    plt.plot(hk.x_value,hk.y_value, c=(000,0.255,0.800),linewidth=5)

    #Emphasize the first and last points.
    plt.scatter(0, 0, c='green',edgecolors='none',s=100)
    plt.scatter(hk.x_value[-1], hk.y_value[-1],c=(0.255,000,000), linewidth=2)

    #remove axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keepRunning = input("Make anotherbwalk?(y/n):")
    if keepRunning == 'n':
        break

