from DebugVisualizer import GraphVisualizer

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value

class Edge:
    def __init__(self, source, target, weight=None):
        self.source = source
        self.target = target
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def add_node(self, id, value):
        node = Node(id, value)
        self.nodes.append(node)
        return node
    
    def add_edge(self, source, target, weight=None):
        edge = Edge(source, target, weight)
        self.edges.append(edge)
        return edge


graph = Graph()

# instance of GraphVisualizer
viz = GraphVisualizer()

# Add nodes
a = graph.add_node(1, "A")
viz.visualize(graph)

b = graph.add_node(2, "B")
viz.visualize(graph)

c = graph.add_node(3, "C")
viz.visualize(graph)

d = graph.add_node(4, "D")
viz.visualize(graph)

# Add edges
graph.add_edge(a, b, 5)
viz.visualize(graph)

graph.add_edge(b, c, 3)
viz.visualize(graph)

graph.add_edge(c, d, 7)
viz.visualize(graph)

graph.add_edge(d, a, 2)
viz.visualize(graph)

graph.add_edge(a, c, 9)
viz.visualize(graph)
