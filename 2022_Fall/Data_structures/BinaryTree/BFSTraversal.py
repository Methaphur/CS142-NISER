# Breadth First Traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def BFS_Traversal(self):
        out = []
        def _BFS(node):
            if node is None:
                return 

            # Stores all nodes at a given level
            # Initializing this with root node
            temp = [node] 

            # All the nodes in a given height
            while temp:
                out.append(temp[0].data)
                node = temp.pop(0)  

                if node.left is not None:
                    temp.append(node.left)

                if node.right is not None:
                    temp.append(node.right)

            return out
        return _BFS(self.root)
    
tree = BinaryTree()
tree.root = Node(2)

tree.root.left = Node(7)
tree.root.right =  Node(5)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(11)

tree.root.right = Node(5)
tree.root.right.right = Node(9)
tree.root.right.right.left = Node(4)

print('BFS Traversal')
print(tree.BFS_Traversal())
