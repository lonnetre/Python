import networkx as nx
import matplotlib.pyplot as plt
import random

def calc_M(matrix):
    row_sums = [sum(row) for row in matrix]
    return [[element / row_sum if row_sum != 0 else 0 for element in row] for row, row_sum in zip(matrix, row_sums)]

def initialize_r(len):
    return [1/len] * len

def calc_M_strich(matrix):
    beta = 0.85
    N = len(matrix)
    return [[beta * element + (1 - beta) * (1 / N) for element in row] for row in matrix]

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def pagerank(A, d, iterations):
    M = []
    # Calculate M from A
    M = calc_M(A)
    
    # Calculate M' = d * M + ...
    M_strich = calc_M_strich(M)

    # Initialize PR
    r = initialize_r(len(M))
    
    # Power Iteration
    M_strich_transpose = transpose(M_strich)

    #...
    
    return -1

def plot_graph(adj_matrix, pageranks):
    # create directed graph from adjacency matrix
    edges = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                edges.append((i, j))
    G = nx.DiGraph(edges)
    for i in range(len(pageranks)):
        if not G.has_node(i):
            G.add_node(i)   
    # set node labels and sizes based on pageranks
    node_sizes, node_labels = [], {}
    for i in G.nodes:
        node_labels[i] = f'{i}\n{pageranks[i]:.2f}'
        node_sizes.append(max(1000, int(10000 * pageranks[i])))
    # set node colors based on pageranks
    node_colors = [(0.0 + pageranks[i], 0.0, 1.0 - pageranks[i], 1.0) for i in G.nodes]
    # plot graph
    pos = nx.spring_layout(G, seed=42, k=1, iterations=10)
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
    nx.draw_networkx_edges(G, pos, connectionstyle='arc3,rad=.1', node_size=node_sizes)
    plt.axis('off')
    plt.show()
    
def generate_random_digraph(V, E):
    adj_matrix = [[0 for j in range(V)] for i in range(V)]
    edges = set()
    while len(edges) < E:
        start_node, end_node = random.randint(0, V-1), random.randint(0, V-1)
        if start_node != end_node:
            edges.add((start_node, end_node))
    for start_node, end_node in edges:
        adj_matrix[start_node][end_node] = 1
    return adj_matrix
    
d, iterations = 0.85, 1000
# Wikipedia:
# Die Ergebnisse fuer das englische und deutsche wiki
# sind fuer den gleichen Graphen scheinbar different
# Dies koennte an der (fehlender) Normierung liegen
adj_matrix_wiki = [
    [0,0,0,0,0,0,0,0,0,0,0],#A
    [0,0,1,0,0,0,0,0,0,0,0],#B
    [0,1,0,0,0,0,0,0,0,0,0],#C
    [1,1,0,0,0,0,0,0,0,0,0],#D
    [0,1,0,1,0,1,0,0,0,0,0],#E
    [0,1,0,0,1,0,0,0,0,0,0],#F
    [0,1,0,0,1,0,0,0,0,0,0],#G
    [0,1,0,0,1,0,0,0,0,0,0],#H
    [0,1,0,0,1,0,0,0,0,0,0],#I
    [0,0,0,0,1,0,0,0,0,0,0],#J
    [0,0,0,0,1,0,0,0,0,0,0],#K
]
adj_matrix_standford = [
    [0,1,1],
    [1,0,1],
    [1,0,0],
]
adj_matrix = generate_random_digraph(8,12)
pageranks = pagerank(adj_matrix_wiki, d, iterations)
plot_graph(adj_matrix_wiki, pageranks)
