import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40)

# Set chart title and lable axes.
plt.title("Square Numbers ", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=10)


# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])
plt.ticklabel_format(useOffset=False)

# Avoid scientific notation
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_scientific(False)

plt.show()
