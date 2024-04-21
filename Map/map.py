import osmnx as ox
import matplotlib.pyplot as plt
ox.settings.log_console = True
# Define the bounding box coordinates (latitude and longitude) for your area of interest
def createmap():
    north, south, east, west = 52.675287, 52.336724, 13.090365, 13.756247 #define bounds of map area

    G = ox.graph_from_bbox(north, south, east, west, network_type='drive') #retrieve map of area from OpenStreetMap

    #plot the map
    fig, ax = ox.plot_graph(G, bgcolor='w', node_color='none', node_edgecolor='none', edge_color='k', edge_linewidth=0.5,show=False, close=False, bbox=(south, north, west, east))

    plt.gcf().set_size_inches(10, 10)
    ax.set_facecolor('black')
    plt.axis('off')
    # Show the plot
    plt.show()

createmap()