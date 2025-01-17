import networkx as nx
	import matplotlib.pyplot as plt

	# making the graph
	G = nx.Graph()
	G.add_edges_from(
		[
			(“A”, “B”, {“weight”: 1}),
			(“A”, “C”, {“weight”: 5}),
			(“A”, “G”, {“weight”: 10}),
			(“B”, “D”, {“weight”: 3}),
			(“G”, “E”, {“weight”: 3}),
			(“D”, “C”, {“weight”: 8}),
			(“C”, “E”, {“weight”: 6}),
			(“D”, “F”, {“weight”: 1}),
			(“C”, “Z”, {“weight”: 9}),
			(“E”, “Z”, {“weight”: 1}),
			(“F”, “Z”, {“weight”: 6}),
		]
	)


#following function is used to findMST, automatically applies Kruskal’s algorithm
	Tree = nx.minimum_spanning_tree(G)

# generating the graph and tree
	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G, pos, node_color = ”blue”, node_size = 450)
	nx.draw_networkx_edges(G, pos, edge_color = “green”)
	nx.draw_networkx_labels(G, pos, font_size = 11, font_family = “sans-serif”)
	nx.draw_networkx_edge_labels(
G, pos, edge_labels = {(u, v): d[“weight”] for u, v, d in G.edges(data = True)}
	)
	nx.draw_networkx_edges(Tree, pos, edge_color = “red”, width = 2)
	plt.axis(“off”)
	plt.show()


