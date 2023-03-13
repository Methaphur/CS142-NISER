'''
Qs1. Create a singly linked list with insert and delete operations at the beginning
and at the end where each node contains an alphabet and a number as data.
'''

# Single linked list , insertion and deletion of elements
class Node:
    def __init__(self,alpha,num):
        self.num_data = num
        self.alpha_data = alpha
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.alpha_data,temp.num_data} ->', end=" ")
            temp = temp.next
        print(None)

    def insert_at_end(self,alpha,num):
        new_node = Node(alpha,num)

        # If no nodes in linked list , make new node the first node
        if self.head is None:
            self.head = new_node
            return 

        # Finding the last node 
        temp = self.head 
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def insert_at_start(self,alpha,num):
        new_node = Node(alpha,num)

        current = self.head 
        self.head = new_node
        new_node.next = current


    def delete_at_start(self):
        if self.head is None: # No nodes to be deleted
            return 

        current = self.head
        self.head = current.next


    def delete_at_end(self):
        if self.head is None: # No nodes to be deleted
            return 

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


list1 = LinkedList()

list1.insert_at_end('A',1)
list1.insert_at_end('B',5)
list1.insert_at_end('C',6)
list1.print_list()


list1.insert_at_start('D',3)
list1.insert_at_start('E',4)
list1.print_list()


list1.delete_at_start()
list1.print_list()

list1.delete_at_end()
list1.print_list()

