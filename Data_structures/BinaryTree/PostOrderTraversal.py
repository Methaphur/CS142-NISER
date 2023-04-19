class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def postorder(self,root):
        out = []
        self._postorder(root,out)
        
        return out

    def _postorder(self,root,out):        
        if not root: # Leaf node 
            return 
            
        self._postorder(root.left,out)     
        self._postorder(root.right,out)
        out.append(root.data)
        
        
print("Post-order Traversal")
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

print(tree.postorder(tree.root))
