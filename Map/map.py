import osmnx as ox
import matplotlib.pyplot as plt
ox.settings.log_console = True
# Define the bounding box coordinates (latitude and longitude) for your area of interest
north, south, east, west = 52.675287, 52.336724, 13.090365, 13.756247
#plt.figure(figsize=(15, 15))
# Download OSM data for the area
G = ox.graph_from_bbox(north, south, east, west, network_type='drive')

#ec = ['b' if data.get('highway') is not None else 'w' for u, v, key, data in G.edges(keys=True, data=True)]


# Plot the map
#fig, ax = ox.plot_graph(G, node_color='none', node_edgecolor='none', node_size=30, edge_linewidth=0.5, edge_color='k', bgcolor='w')
#plt.figure(figsize=(15, 15))
fig, ax = ox.plot_graph(G, bgcolor='w', node_color='none', node_edgecolor='none', edge_color='k', edge_linewidth=0.5,show=False, close=False, bbox=(south, north, west, east))
# Add grid lines
#ax.grid(True)
plt.gcf().set_size_inches(10, 10)
# Add labels and title
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.title('Map of the Area')
ax.set_facecolor('black')
plt.axis('off')
# Show the plot
plt.show()
