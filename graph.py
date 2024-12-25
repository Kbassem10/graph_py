#Karim Bassem Joseph

import networkx as nx
import matplotlib.pyplot as plt

'''
getting input from the user with the number of nodes and the number of edges between them
for example: 
A -- B
|  \ |
C -- D
number of links = 5
number of nodes = 4
'''
n = int(input("The number of Nodes: "))
m = int(input("The Number of links: "))

#this line below creates a matrix (2D array) with all of the items set to 0 
# the loop is responsible to make it 2D and the * to make the 0
adj_matrix = [[0] * (n+1) for i in range(n + 1)]

#a loop to take the input from the user with all of the edges U and V the two edges
for i in range(m):
    u = int(input("U: "))
    v = int(input("V: "))

    #assign the number 1 to the places of the 2D array
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

print("The Adjacent Matrix: ")

#loop to print the 2D array but to make every row alone and remove the row number 0
for i in adj_matrix[1:]:
    print(i[1:])

#creates the graph
G = nx.Graph()

#a nested loops that iterates on all of the 2D array to checks the ones and draw an edge between them
for i in range(1, n+1):
    for j in range(1, n+1):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)

#draw the graph 
nx.draw(G, with_labels=True)
#show the graph
plt.show()

#function to count the possible paths between 2 points
def count_paths(adj_matrix, start, end, visited):
    #the base case checks to return 1 on the recurion
    if start == end:
        return 1
    
    #make the current start to be True on the array of visisted so we don't count this path again
    visited[start] = True

    #setting the counter to 0 path
    count = 0

    #a loop to iterate over the collumns of the 2D array
    for current in range(1, n + 1):
        #checks if the current element that you are on is 1 (means have an edge) and not visited before
        if adj_matrix[start][current] == 1 and not visited[current]:
            #call the function again with that edge if you haven't visited it before and when it returns the bas case the count will be incremented by 1
            count += count_paths(adj_matrix, current, end, visited)
    #after finishing the loop making the current start = False again so you can go on it again
    visited[start] = False

    #returnin the total count of paths between 2 points
    return count

#input the start to start counting from
start = int(input("Start of counting: "))

#input the end to stop counting on it
end = int(input("End of counting: "))

#creating a list of False and that list is the size as the number of nodes + 1 that means that there is nothing visited before
visited = [False] * (n + 1)

#calling the function of counting the paths
path_count = count_paths(adj_matrix, start, end, visited)

#prints the number of paths
print(f"Number of paths between {start} and {end}: {path_count}")
