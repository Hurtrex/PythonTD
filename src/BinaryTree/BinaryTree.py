from src.BinaryTree.BinaryTreeNode import BinaryTreeNode

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,parent_key,child_key,value,direction=None):
        if self.root is None:
            self.root = BinaryTreeNode(child_key,value)
            return
        parent = self.find(parent_key)
        if parent is None:
            print("error")
            return
        if direction == 'left':
            if parent.left is None:
                parent.left = BinaryTreeNode(child_key,value)
                return
            else:
                print("error")
        elif direction == 'right':
            if parent.right is None:
                parent.right = BinaryTreeNode(child_key,value)
                return
            else:
                print("error")
        else:
            print("error")

#IMPORTANT WILL BE AT THE EXAM PRACTICE FOR SURE
#level wise is always a queue
#depth first is a stack
    def find_levelwise(self,key):
        to_visit = Queue()
        to_visit.equeue(self.root)
        while not to_visit.isEmpty():
            visited = to_visit.dequeue()
            if visited.key == key:
                return visited
            queue.enqueue(visited.left)
            queue.enqueue(visited.right)
        return None

    def find_depthfirst(self, key):
        if self.root is None:
            #just mean the tree doesnt exist
            return None
        return self.find_recursive(self.root, key)
    #or return self.find_iterative(self.root, key)
    #now we know the tree exist we start at the root with the key

    def find_recursive(self, start, key):
        if start is None:
            return None
        if start.key == key:
            #we check the key if the key is the right one we return start aka the node
            return start
        result = self.find_recursive(start.left, key)
        if result is None:
            return self.find_recursive(start.right, key)
        return result
    #Basically it checks the left if its the good key if its not
    #it becomes the new  start, and then we recheck the left key
    #we repeat until it gets to the bottom then it goes back to the right

    def find_iterative(self, start, key):
        to_visit = stack()
        to_visit.push(start)
        while not to_visit.isEmpty():
            visited = to_visit.pop()
            if visited.key == key:
                return visited
            if not None:
                to_visit.push(visited.right)
            if not None:
                to_visit.push(visited.left)
        return None

    #to make this to work with n number of children we do a while for the push
    #loop that pushes all children
