# Question 1 
# List contains 2s and 1s , find the index where transition occurs

def transition(arr, left, right):
    # List has been traversed through and no such transition exists
    if left > right:
        return False

    # if mid-element is 2 and prev element is 1 , transition occurred
    mid = (left + right) // 2
    if arr[mid] == 2:
        if arr[mid - 1] == 1:
            return mid
        else:
            # Call the function again on left part of list
            return transition(arr, left, mid - 1)
    else:
        # call the function on right part of the list
        return transition(arr, mid + 1, right)
        
list1 = [1, 1, 1, 2, 2, 2, 2]
print("Qs 1 ")
print(list1)
print('Trasition Index: ',end='')
print(transition(list1, 0, len(list1)))
print()

# Question 2 
# Find the middle element of a linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    # Utility function to add a node at head
    def add(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        node.next = temp
    
    # Utility function to print the linked list
    def printlist(self):
        temp = self.head
        while temp:
            print(f'{temp.data}-> ',end="")
            temp = temp.next
        print('None')        
        
    
    # Logic is to use a fast pointer and a slow pointer
    # Fast pointer moves at 2 speed while slow pointer moves at one speed
    # When fast pointer reaches the end , slow pointer would've reached middle
    def find_middle(self):
        if self.head is None:
            return None
        
        slowPointer = self.head
        fastPointer = self.head
        
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            
        return slowPointer.data
    

print("Qs 2.")
chain = LinkedList()
chain.add(1)
chain.add(2)
chain.add(3)
chain.add(4)
chain.add(5)
chain.printlist()
print('Middle Index: ',end='')
print(chain.find_middle())
