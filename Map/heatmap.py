import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors

input_file = "Accident_data/accidents19and21_with_quadrants.csv" # The input file
input_data = pd.read_csv(input_file) # Read the data
data_len=len(input_data)
input_data['quadrant']= np.zeros(data_len) 

berlin_latitude_range = (52.336724, 52.675287) # Latitude range for Berlin
berlin_long_range = (13.090365, 13.756247) # Longitude range for Berlin
multiplication_factor = 100
lat_range = (float(berlin_latitude_range[0] * multiplication_factor), float(berlin_latitude_range[1] * multiplication_factor)) # Multiply the latitude range by the multiplication factor
lon_range = (float(berlin_long_range[0] * multiplication_factor), float(berlin_long_range[1] * multiplication_factor)) # Multiply the longitude range by the multiplication factor
grid = np.zeros((100,100)) # Create a grid of zeros with the size of the multiplication factor
quadrant_count = pd.read_csv('Accident_data/quadrant_counts_19and21.csv', sep=',') # Read the quadrant counts
for index, row in quadrant_count.iterrows(): # Iterate over the quadrant counts
    quadrant = row['quadrant'] # Get the quadrant
    row_idx = int(quadrant // multiplication_factor) # Get the row index 
    col_idx = int(quadrant % multiplication_factor) # Get the column index
    grid[row_idx, col_idx] = row['count'] # Set the grid value to the count

# Create a custom colormap
cmap = plt.cm.get_cmap('plasma')
cmap_colors = cmap(np.arange(cmap.N))
cmap_colors[0] = (0, 0, 0, 0)  # Set the lowest value to be transparent
custom_cmap = mcolors.ListedColormap(cmap_colors)
step = 100
lat=np.linspace(lat_range[0],lat_range[1],step)  # Create a linear space for latitude
lon=np.linspace(lon_range[0],lon_range[1],step) # Create a linear space for longitude
map_image = plt.imread('Map/map.jpg')  # Adjust the extent according to your map coordinates

plt.figure(figsize=(20, 10)) # Set the figure size
plt.imshow(map_image,  extent=[lon_range[0], lon_range[1], lat_range[0], lat_range[1]]) # Plot the map image


# Plot grid lines
for x in lat:
    plt.plot([lon_range[0], lon_range[1]], [x, x], color='none', alpha=0.5, linewidth=0.5)

for y in lon:
    plt.plot([y, y], [lat_range[0], lat_range[1]], color='none', alpha=0.5, linewidth=0.5)

# Add grid labels
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(100))  # Adjust the tick frequency as needed
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(100))  # Adjust the tick frequency as needed

plt.imshow(grid, cmap=custom_cmap, alpha=0.4, extent=[lon_range[0], lon_range[1], lat_range[0], lat_range[1]]) # Plot the heatmap

plt.colorbar(label='Accident Rate')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Accident Heatmap')
plt.show()