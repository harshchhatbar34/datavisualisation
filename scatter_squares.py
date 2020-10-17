import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Greens, edgecolor='none', s=40)
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

#set the range of each axis
plt.axis([0,1100,0,1100000])
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
