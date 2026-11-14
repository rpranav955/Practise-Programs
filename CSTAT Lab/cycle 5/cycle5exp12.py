from mpl_toolkits.mplot3d import Axes3D
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

sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

continents = list(sorted_data.keys())
areas = list(sorted_data.values())

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(continents, areas, color='lightgreen', edgecolor='black')


ax.set_xlabel('Continents', fontsize=12)
ax.set_ylabel('Area (Million sq km)', fontsize=12)
ax.set_title('Area of Continents', fontsize=14)


plt.xticks(rotation=45, ha='right')


for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval}', ha='center', va='bottom', fontsize=10)


plt.tight_layout()

plt.show()
