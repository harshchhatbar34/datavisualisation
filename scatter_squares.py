import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
plt.scatter(x_value, y_value, s=200, c='black')
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
