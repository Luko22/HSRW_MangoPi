import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
input_file = "accidents_Berlin_2021.csv"
input_data = pd.read_csv(input_file)
#input_data = input_data.head(5)
data_len=len(input_data)
input_data['quadrant']= np.zeros(data_len)
# berlin latitude range:52.33,52.67
# berling long range:13.0-13.75
berlin_latitude_range = (52.336724, 52.675287)
berlin_long_range = (13.090365, 13.756247)
multiplication_factor = 100
lat_range = (int(berlin_latitude_range[0] * multiplication_factor), int(berlin_latitude_range[1] * multiplication_factor))
lon_range = (int(berlin_long_range[0] * multiplication_factor), int(berlin_long_range[1] * multiplication_factor))
grid = np.zeros((100,100))
quadrant_count = pd.read_csv('quadrant_counts.csv', sep=',')
for index, row in quadrant_count.iterrows():
    quadrant = row['quadrant']
    row_idx = int(quadrant // multiplication_factor)
    print(row_idx)
    col_idx = int(quadrant % multiplication_factor)
    print(col_idx)
    grid[row_idx, col_idx] = row['count']

data = np.random.rand(len(lat_range), len(lon_range))

cmap = plt.cm.get_cmap('plasma')
cmap_colors = cmap(np.arange(cmap.N))
cmap_colors[0] = (0, 0, 0, 0)  # Set the lowest value to be transparent
custom_cmap = mcolors.ListedColormap(cmap_colors)
step = 100
lat=np.linspace(lat_range[0],lat_range[1],step)
#lat_range=lat_range.flatten()
lon=np.linspace(lon_range[0],lon_range[1],step)
map_image = plt.imread('map.jpg')  # Adjust the extent according to your map coordinates
plt.imshow(map_image, extent=[lon.min(), lon.max(), lat.min(), lat.max()])


print(lon.min())
print(lon.max())
print(lat.min())
print(lat.max())

# Plot grid lines
for x in lat:
    plt.plot([lon.min(), lon.max()], [x, x], color='black', alpha=0.5, linewidth=0.5)

for y in lon:
    plt.plot([y, y], [lat.min(), lat.max()], color='black', alpha=0.5, linewidth=0.5)

# Add grid labels
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))  # Adjust the tick frequency as needed
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(20))  # Adjust the tick frequency as needed

plt.imshow(grid, cmap=custom_cmap, alpha=0.4, extent=[lon_range[0], lon_range[1], lat_range[0], lat_range[1]])

#plt.colorbar(label='Accident Rate')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Accident Heatmap')
plt.show()