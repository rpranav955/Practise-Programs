import matplotlib.pyplot as plt

data = {
    'Asia': 13.4,
    'Africa': 11.73,
    'North America': 9.54,
    'South America': 6.89,
    'Antarctica': 5.41,
    'Europe': 3.93,
    'Australia/Oceania': 3.29
}


plt.bar(data.keys(), data.values(), color = 'lightgreen', edgecolor = 'black')

plt.title("Area of Continents")
plt.xlabel("Continents")
plt.ylabel("Area (Million sq. miles)")

plt.show()
