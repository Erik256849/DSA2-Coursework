import networkx as nx
import matplotlib.pyplot as plt

# making the graph
G = nx.Graph()
G.add_edges_from(
    [
        ("A", "B", {"weight": 1}),
        ("A", "C", {"weight": 5}),
        ("A", "G", {"weight": 10}),
        ("B", "D", {"weight": 3}),
        ("G", "E", {"weight": 3}),
        ("D", "C", {"weight": 8}),
        ("C", "E", {"weight": 6}),
        ("D", "F", {"weight": 1}),
        ("C", "Z", {"weight": 9}),
        ("E", "Z", {"weight": 1}),
        ("F", "Z", {"weight": 6}),
    ]
)

# following function is used to find MST, automatically applies Kruskal’s algorithm
Tree = nx.minimum_spanning_tree(G)

# generating the graph and tree
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color="blue", node_size=450)
nx.draw_networkx_edges(G, pos, edge_color="green")
nx.draw_networkx_labels(G, pos, font_size=11, font_family="sans-serif")
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
)
nx.draw_networkx_edges(Tree, pos, edge_color="red", width=2)
plt.axis("off")
plt.show()

# QuickSort implementation

def partition(array, low, high):
    pivot = array[high - 1]  # this selects pivot as second-to-last element of array
    i = low - 1
    for j in range(low, high - 1):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]  # swapping array elements
    array[i + 1], array[high - 1] = array[high - 1], array[i + 1]  # input pivot in spot
    return (i + 1)


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


# Testing quicksort with a list of strings
arr = ["cat", "dog", "tiger", "lion", "monkey"]
quicksort(arr, 0, len(arr))
print("The array has been sorted:", arr)
