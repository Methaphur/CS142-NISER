# Question 1 
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
        

print("Qs 1. In-order Traversal")
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
print()

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def inorder(self,root):
        out = []
        self._inorder(root,out)
        return out

    def _inorder(self,root,out):        
        if not root: # Leaf node 
            return 
            
        self._inorder(root.left,out) 
        out.append(root.data)    
        self._inorder(root.right,out)

    def find_operator(self,arr):
        left = 0
        right = 0
        for i in range(1,len(arr)-1):
            if arr[i] == "(":
                left += 1
            if arr[i] == ")":
                right += 1
            if left == right:
                return i + 1
        for i in arr:
            if i in '+-x/':
                return arr.index(i)
        
        return -1

    def operation(self,n1,n2,operator):
        if operator == "+":
            return n1 + n2
        if operator == "-":
            return n1 - n2
        if operator == "x":
            return n1 * n2
        if operator == "/":
            return n1 / n2
        print("Operation not possible! ")
    
    def CreateTreeFromList(self,arr,node):
        # Adding a root node
        if not node:
            node = Node("None")
            self.root = node

         # Base case
        if len(arr) == 1:
            node.data = (arr[0])
            return 

        # Finding the middle operator 
        mid =   self.find_operator(arr)    
        node.data = arr[mid]        
        node_left = Node("None")    # Dummmy nodes
        node_right = Node("None")   # Dummy nodes

        # Setting root as parent of left and right nodes
        node.left = node_left    
        node.right = node_right

        # Solving left and right nodes
        self.CreateTreeFromList(arr[1:mid],node_left)
        self.CreateTreeFromList(arr[mid+1:-1],node_right)

    def solve(self,node):
        # Finding operator node
        if not (node.left or node.right):  
            return node.data

        operator = node.data
        left_operand = self.solve(node.left)
        right_operand = self.solve(node.right)
        result = self.operation(left_operand,right_operand,operator)        
        
        return result 
    

print("Qs 2. Expression to Tree")
expression =  ['(', '(', 3, '+', 5, ')', 'x', '(', 4, 'x', 2, ')', ')']

operation = BinaryTree()
operation.CreateTreeFromList(expression,operation.root)
print(f'In-order : {operation.inorder(operation.root)}')
print(f'Solved: {operation.solve(operation.root)}')