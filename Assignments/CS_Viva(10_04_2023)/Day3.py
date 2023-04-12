# Baby step problem modified 
# Recursive program to count the number of ways to reach n'th step 
# i'th position to i+1 or i^2 

def count(n):
    # f(n) = f(n-1) + f(sqrt(n)) n is perfect square
    # f(n) = f(n-1) else
    
    if n < 2:
        return 1
        
    if n**0.5 == int(n**0.5):
        return count(n-1) + count(int(n**0.5))
    else:
        return count(n-1)

print("Qs 1.")
n = 9
print("n = ",n)
print("Number of ways: ",count(n))
print()

# Inserting node at i'th position in a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Utility function 
    def add(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        node.next = temp

    # Utility function to print the elements
    def printlist(self):
        temp = self.head
        while temp:
            print(f'{temp.data}-> ',end="")
            temp = temp.next
        print("None")
        
        
    def insert_ith(self,index,data):
        node = Node(data)
        
        if self.head is None:
            if index != 0:
                print('Index out of Range')
                return 
            
        if index == 0:
            temp = self.head
            self.head = node
            node.next = temp
            return
        
        count = 1 
        temp = self.head
        while temp.next:
            if count == index:
                next = temp.next
                temp.next = node
                node.next = next
                return
            else:
                count += 1
                temp = temp.next

        print('Index out of range')

print("Qs 2.")
chain = LinkedList()
chain.add(1)
chain.add(2)
chain.add(3)
chain.add(4)
chain.printlist()

chain.insert_ith(3,5)
chain.printlist()
