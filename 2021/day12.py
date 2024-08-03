from collections import defaultdict

class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.unique_paths = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, d, visited, path, flag=False):
        # Mark the current node as visited and store in path
        visited[u] += 1
        if u.islower() and visited[u] >= 2:
            flag = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            self.unique_paths += 1
            # print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if i in ['start', 'end']:
                    if visited[i] >= 1:
                        continue
                if i.islower() and i not in ['start', 'end']:
                    if flag and visited[i] >= 1:
                        continue
                self.printAllPathsUtil(i, d, visited, path, flag)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] -= 1

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
        visited = {}
        for node in self.graph.keys():
            visited[node] = 0

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


# Create a graph given in the above diagram
g = Graph()
matches = {}
with open('input.txt', 'r') as file:
    text = list(file.readlines())

for lines in text:
    line = lines.strip()
    src, des = line.split('-')
    g.addEdge(src, des)
    g.addEdge(des, src)

g.printAllPaths('start', 'end')
print(g.unique_paths)