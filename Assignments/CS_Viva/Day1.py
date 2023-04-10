# Question 1
# Recursive program to count the number of ways to reach the nth step
# Move to (i+1) th step or (i + i)th step

def count(n):
    # f(n) = f(n-1)  n is odd
    # f(n) = f(n-1) + f(n/2) n is even
    if n <= 2:
        return 1
        
    if n%2 == 0:
        return count(n-1)
    else:
        return count(n-1) + count(n/2)

print("Qs 1.")
n = 4
print("n = ",n)
print("Number of ways: ",count(n))
print()

# Question 2
# Deleting i'th element in a linked list
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

    def delete_ith(self,index):
        temp = self.head
        if not temp:
            print("List Index Out of Range")
            return
        
        if index == 0:
            self.head = temp.next
            return
        
        count = 1
        while temp.next:
            if count == index:
                temp.next = temp.next.next
                return
            count += 1
            temp = temp.next
            
        print("List Index Out of Range")


print("Qs 2.")
chain = LinkedList()
chain.add(1)
chain.add(2)
chain.add(3)
chain.add(4)
chain.printlist()
chain.delete_ith(2)
chain.printlist()
