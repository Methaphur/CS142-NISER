# Question 1 
# Write a Recursive program to output all the subsets of a given set

def subset_gen(array):
    out = []
    def _subset(array,arr=[],index=0):
        # Base condition
        if index == len(array):
            out.append(arr)
            return
    
        else:
            _subset(array,arr+[array[index]],index+1)  # Current element is included
            _subset(array,arr,index+1)    # Current element is excluded
    
    _subset(array,arr=[],index=0)
    return out

print('Qs 1.')
array = [1,2,3]
print(subset_gen(array))

# Question 2 
# Make a linked list with even number of elements
# Cut the linked list into two halves and compare the two lists

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    # Utility function to add elements to list
    def add(self,data):
        node = Node(data)
        temp = self.head
        self.head = node
        node.next = temp
    
    # Utility function to print elements
    def printlist(self):
        temp = self.head
        while temp:
            print(f'{temp.data} -> ',end="")
            temp = temp.next
        print('None')


# Accepts head of a linked list and breaks into two halves
def breakchain(head):
    slowPointer = head
    fastPointer = head

    while fastPointer.next and fastPointer.next.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    
    mid = slowPointer.next  # Storing head of second half 
    slowPointer.next = None  # Breaking linked list
    return mid

# Function to compare two linked lists
def compare(head1,head2):
    while head1 and head2:
        # Traversing both the linked lists simultaneously and comparing current nodes
        if head1.data != head2.data:
            print('Linked Lists are not Identical')
            return False
         
        head1 = head1.next
        head2 = head2.next

    print('Linked Lists are Identical')
    return True

print("\nQs 2.")

chain1 = LinkedList()
chain1.add(1)
chain1.add(2)
chain1.add(3)
chain1.add(4)
chain1.add(5)
chain1.add(6)
chain1.printlist()

chain2 = LinkedList()   # Creating second half
chain2.head = breakchain(chain1.head) # Setting head of second half as mid 
chain1.printlist()
chain2.printlist()
print()

print(compare(chain1.head,chain2.head))

# Signing off 
# Harisankar <3 
