import matplotlib.pyplot as plt
from matplotlib import style

# ------------------ Simple Line Plot ------------------
plt.plot([1, 2, 3], [2, 5, 3])
plt.show()

# ------------------ Points Plot ------------------
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()

# ------------------ Categorical Plotting ------------------
names = ['Abhishek', 'Krishna', 'Jayesh']
marks = [87, 54, 98]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, marks)
plt.title("Bar Chart")

plt.subplot(132)
plt.scatter(names, marks)
plt.title("Scatter Plot")

plt.subplot(133)
plt.plot(names, marks)
plt.title("Line Plot")

plt.suptitle('Categorical Plotting')
plt.show()

# ------------------ Styled Line Graph ------------------
style.use('ggplot')

x = [16, 8, 10]
y = [8, 16, 6]
x2 = [8, 15, 11]
y2 = [6, 15, 7]

plt.plot(x, y, color='red', label='Line One', linewidth=3)
plt.plot(x2, y2, color='magenta', label='Line Two', linewidth=3)

plt.title('Epic Info')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)
plt.show()
