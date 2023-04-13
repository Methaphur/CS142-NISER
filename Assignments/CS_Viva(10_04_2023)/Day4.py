# Question 1
# Recursive program to count the number of ways to reach the nth step
# i step to i+1 step or 2n step or 3n step

def count(n):
    # f(n) = f(n-1) + f(n/2) + f(n/3) n is multiple of 6 ( 2 and 3)
    # f(n) = f(n-1) + f(n/2) n is multiple of 2
    # f(n) = f(n-1) + f(n/3) n is mutliple of 3
    # f(n) = f(n-1) else
    
    if n <= 2:
        return 1
        
    if n%2 == 0 and n%3 == 0:
        return count(n-1) + count(n/2) + count(n/3)
    elif n%2 == 0:
        return count(n-1) + count(n/2)
    elif n%3 == 0:
        return count(n-1) + count(n/3)
    else:
        return count(n-1)

print("Qs 1.")
n = 4
print("n = ",n)
print("Number of ways: ",count(n))
print()

# Question 2
# Swapping i , i+1 th element of a linked list

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
    
    def swap_ith(self,index):
        if self.head is None:
            print('Index out of Range')
            return
        
        if index == 0:
            temp = self.head
            swap = temp.next
            next = swap.next
            
            self.head = swap
            swap.next = temp
            temp.next = next
            return
            
        count = 1
        temp = self.head
        while temp.next and temp.next.next:
            if count == index:
                curr = temp.next
                prev = temp
                next = curr.next.next
                
                prev.next = curr.next
                curr.next.next = curr 
                curr.next = next
                return 
            
            count += 1
            temp = temp.next
        print('List Index Out of Range')
    
    def extend(self,data):
        for data in data:
            self.add(data)
            
print('Qs 2.')
chain = LinkedList()
chain.add(1)
chain.add(2)
chain.add(3)
chain.add(4)
chain.add(5)

chain.printlist()
chain.swap_ith(2)
chain.printlist()
