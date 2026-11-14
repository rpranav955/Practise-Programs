import matplotlib.pyplot as plt

heights = [150, 155, 160, 162, 165, 168, 170, 172, 175, 180, 160, 165, 165]

plt.hist(heights, bins=5, color='lightgreen', edgecolor='black')

plt.xlabel("Height (cm)")
plt.ylabel("Number of students")
plt.title("Histogram of Classmate's Heights")

plt.show()

