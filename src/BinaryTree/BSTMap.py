from src.BinaryTree import BST_Node


class BSTMap:
    def __init__(self):
        self.root = None

    def put(self, k, v):
        new_node = BST_Node(k,v)
        if self.root is None:
            self.root = new_node
            return
        self.attach(self.root, new_node)

    def attach(self,start, new_node):
        if start.key == new_node.key:
            start.value = new_node.value
            return
        if new_node.key < start.key:
            if start.left is None:
                start.left = new_node
            else:
                self.attach(start.left, new_node)
        else:
            if start.right is None:
                start.right = new_node
            else:
                self.attach(start.right, new_node)

    def remove(self, key):
        node_to_delete = self.find(key)
        parent_left_most = find_parent_of_left_most(node_to_delete.right)

        node_to_delete.key = parent_left_most.key
        node_to_delete.value = parent_left_most.value
        parent_left_most.left = None

    def find(self, key):
        if self.root is None:
            return None
        runner = self.root
        while runner.key != key and runner is not None:
            if runner.key > key:
                runner = runner.left
                continue
            if runner.key < key:
                runner = runner.right
                continue
            return runner
        return runner
#since we have "find" which get the node (so everything) we can do
# get easily
    def get(self,k):
        found = self.find(k)
        if found is not None:
            return found.value
        return None

#FPLM
    def find_parent_of_left_most(self,start):
        runner = start
        while runner.left is not None:
            runner = runner.left

        return runner

