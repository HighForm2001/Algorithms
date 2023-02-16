class Graph:
    nodes:dict
    edges:set

    def __init__(self):
        self.nodes = dict()
        self.edges = set()

if __name__ == "__main__":
    g = Graph()
    print(g)