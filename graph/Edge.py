from graph.Node import Node


class Edge:
    weight:int
    from_node:Node
    to_node:Node

if __name__ == "__main__":
    edge = Edge()
    print(edge)