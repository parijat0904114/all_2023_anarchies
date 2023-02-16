from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.g = defaultdict(list)

    def insert(self, node1, node2):
        self.g[node1].append(node2)

    def full_graph(self):
        print(dict(self.g))

    def edges_of_a_node(self, node):
        if self.g[node]:
            for n in self.g[node]:
                print(node, n)


graph = Graph()
graph.insert(1,2)
graph.insert(1,4)
graph.insert(1,6)
graph.insert(1,9)
graph.insert(2,3)
graph.insert(2,4)
graph.insert(3,4)
graph.insert(4,6)
graph.full_graph()
graph.edges_of_a_node(2)

# Sample output:
# {1: [2, 4, 6, 9], 2: [3, 4], 3: [4], 4: [6]}
# 2 3
# 2 4