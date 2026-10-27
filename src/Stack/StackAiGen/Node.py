class Node:
    """One item in the stack. Points to the node underneath it."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
