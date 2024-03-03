# Question 1
''' Write a program to do BFS Traversal using a list'''
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
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.left.left = Node(4)
tree.root.left.right = Node(8)
tree.root.left.left.left = Node(1)
tree.root.right = Node(30)
tree.root.right.right = Node(40)
print('Qs 1. BFS Traversal')
print(tree.BFS_Traversal())
print()

# Question 2 
'''Generate all permutations of a string using a recursive program. An example given below
for the input =’abc’.'''

def permute(string):
    permutations= []
    def _permute(string,out):
        # If length of string is 0 , Out will have one permuations
        if not len(string):
            permutations.append(out) 

        # Iterating through all the elements in list and permuting with the rest
        for index,item in enumerate(string):
           _permute(string[:index] + string[index+1:], out + item)

    _permute(string,"")
    return permutations

print('Qs 2. Permutations')
string = 'abc'
print(f'String: {string}')
print(permute(string))
print()

# Question 3 
'''Reverse a linked list'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(f'{temp.data} ->',end=" ")
            temp = temp.next
        print("None")
    
    def add(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        node.next = temp
    
    def extend(self,data):
        for data in data:
            self.add(data)

    def reverse(self):
        curr = self.head
        prev = None
    
        while curr:
            next = curr.next
            curr.next =  prev
            prev = curr
            curr = next
        
        self.head = prev

print('Qs 3. Reversing Linked List')
chain = LinkedList()
chain.extend([1,2,3,4])
chain.printlist()
chain.reverse()
chain.printlist()
