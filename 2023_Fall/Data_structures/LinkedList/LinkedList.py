class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,node_data):
        node = Node(node_data)
        curr = self.head
        self.head = node
        node.next = curr
        
    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} -> ',end='')
            temp = temp.next
        print('None')
    
    def append(self,node_data):
        node = Node(node_data)
        
        if self.head is None:
            self.head = node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        
    # Inserting node at i'th position
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
        while temp:
            if count == index:
                next = temp.next
                temp.next = node
                node.next = next
                return
            else:
                count += 1
                temp = temp.next

        print('Index out of range')    
    
    def delete_last(self):
        if self.head is None:
            return
        
        temp = self.head
        while temp.next.next: # Second last element 
            temp = temp.next
        
        temp.next = None

    # Deleting i'th element in list
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
     
    def extend(self,data): # Appending a list as nodes    
        for node_data in data:
            self.append(node_data)
        
    def delete_start(self):
        if self.head is None:
            return 
        
        temp = self.head
        self.head = temp.next
    
    # Finding middle of a list from a particular node (head here)
    def find_middle(self,head):
        if head is None:   
            return head
        
        slowPointer = head
        fastPointer = head
        
        while fastPointer.next and fastPointer.next.next:
            slowPointer = slowPointer.next      # Slow pointer traversing one node at a time
            fastPointer = fastPointer.next.next # Fast pointer going through 2 nodes at a time 
    
        return slowPointer
    
    
    # Reversing a linked list
    def reverse_list(self):
        current = self.head
        prev = None
    
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    
    def find_nth(self,index):   # Finding nth element in a linked list
        count = 0
        current = self.head
        
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
            
        return 'List index out of range'
        
    def find_k(self,K):         # Finding index of k in list
        current = self.head
        count = 0
        while current:
            if current.data == K:
                return count
            
            current = current.next
            count += 1
            
        return f"{K} doesn't exist in list"
    
    def length(self):
        count = 1
        current = self.head
        while current.next:
            current = current.next
            count += 1
        
        return count


list1 = LinkedList()
list1.add(4)             # Added 4 at the start
list1.add(3)
list1.print_list()          
list1.append(5)          # Added 5 at the end 
list1.print_list()
list1.insert_ith(3,6)   # Adding 6 to 3rd index
list1.print_list()
list1.delete_last()      # Deleted the 6 at the end
list1.print_list()
list1.delete_ith(2)     # Deleting 5 at 2nd index 
list1.print_list()
list1.extend([1,2,3,4,5])# Adds a list of node_data
list1.print_list()
list1.delete_start()     # Deletes node 3 in list
list1.print_list()
list1.delete_start()     # Deletes node 4 in list
list1.print_list()
print(list1.find_middle(list1.head).data,' - mid') # Printing data of middle element 
list1.reverse_list()     # Reversing a linked list
list1.print_list()
print(list1.find_nth(1) , "(index = 1)") # Finding element of nth index in linked list
print(list1.find_k(4) , "(K = 4)")       # Finding index of K in the linked list              
print(list1.length())    # Returning length of linked list
