import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]
plt.title("Cubes Number", fontsize=24)
plt.xlabel("values", fontsize=20)
plt.ylabel("cubes of values", fontsize=20)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=100)
plt.tick_params()
plt.show()

