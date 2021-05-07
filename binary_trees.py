'''
https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

A. Tree represents the nodes connected by its edges
    1. Non-linear data structure
    2. One node is marked as Root node
    3. Every node other than the root is associated with one parent node
    4. Each node can have arbitrary number of child
'''

# Designate one node as the root node and then add more nodes as child nodes
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''
        Insert leaves into a tree. 
        Compares new value of the node to the parent node and decides to ass it as a
        left node or a right node
        '''
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        '''
        Prints the tree
        '''
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

# Traversal is the process of visiting all the nodes of a tree and may print values
# Because all nodes are connected via edges (links) we always start from the root
# Cannot access a a random node in a tree

    def inorderTraversal(self, root):
        '''
        First, visit left subtree, then the root, then later the right subtree
        Left -> Root -> Right
        '''
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        '''
        Root -> Left ->Right
        '''
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        '''
        Left ->Right -> Root
        '''
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))