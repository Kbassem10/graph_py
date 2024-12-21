import networkx as nx
import matplotlib.pyplot as plt

n = int(input("The number of Nodes: "))
m = int(input("The Number of edges: "))

adj_matrix = [[0] * (n+1) for i in range(n + 1)]

for i in range(m):
    u = int(input("U: "))
    v = int(input("V: "))
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

print("The Adjacent Matrix: ")
for i in adj_matrix[1:]:
    print(i[1:])

G = nx.Graph()

for i in range(1, n+1):
    for j in range(1, n+1):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)

nx.draw(G, with_labels=True)
plt.show()

def count_paths(adj_matrix, start, end, visited):
    if start == end:
        return 1
    visited[start] = True
    count = 0
    for current in range(1, n + 1):
        if adj_matrix[start][current] == 1 and not visited[current]:
            count += count_paths(adj_matrix, current, end, visited)
    visited[start] = False
    return count

start = int(input("Start of counting: "))
end = int(input("End of counting: "))

visited = [False] * (n + 1)
path_count = count_paths(adj_matrix, start, end, visited)
print(f"Number of paths between {start} and {end}: {path_count}")
