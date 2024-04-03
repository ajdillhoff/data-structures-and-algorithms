import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
# G.add_edge(1, 5)
G.add_edge(2, 3)
# G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(5, 6)
# G.add_edge(2, 6)

# explicitly set positions
pos = {
    1: (0, 1),
    2: (1, 0),
    3: (1, 2),
    4: (2, 2),
    5: (2, 0),
    6: (3, 1),
}

options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)
# nx.draw_networkx(G, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

G_mst = nx.minimum_spanning_tree(G)

nx.draw_networkx(G_mst, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()