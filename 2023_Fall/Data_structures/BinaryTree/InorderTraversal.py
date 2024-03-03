class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder(self,root):
        in_out = []
        self._inorder(root,in_out)
        
        return in_out

    def _inorder(self,root,in_out):        
        if not root: # Leaf node 
            return 
            
        self._inorder(root.left,in_out)     
        in_out.append(root.data)
        self._inorder(root.right,in_out)
        

print("In-order Traversal")
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

print(tree.inorder(tree.root))   # Inorder traversal
