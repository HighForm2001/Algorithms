class Node:
    value: int
    in_val: int
    out_val: int
    nexts: list
    edges: list

    def __init__(self, val: int):
        self.value = val
        self.in_val = 0
        self.out_val = 0
        self.nexts = []
        self.edges = []


if __name__ == "__main__":
    node = Node(1)
    print(node)
