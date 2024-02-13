class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} ->', end=" ")
            temp = temp.next
        print(None)
    

    def append(self,alpha):  # same as insert_at_end()
        new_node = Node(alpha)
        
        if self.head is None:
            self.head = new_node
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
    
    def extend(self,data): # Appending a list
        for data in data:
            self.append(data)

    # Finding middle element of linked list starting from head
    def find_middle(self,head): 
        if head is None: # Empty linked list
            return head
        
        slow_node = head # Traverses one node at a time 
        fast_node = head # Traverses two nodes at a time 
        
        while fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return slow_node

    # Same logic of merge sort in arrays
    def merge_sort(self,head):
    
        if head.next is None:
            out = LinkedList()
            out.append(head.data)
            return out

        mid = self.find_middle(head) # Left side of linked list
        mid_next = mid.next          # Right side of linked list
        mid.next = None
    
        left_list = self.merge_sort(head)
        right_list = self.merge_sort(mid_next)

        return self.merge(left_list,right_list)


    def merge(self,left,right):
        out = LinkedList() # Empty linked list

        temp_left = left.head
        temp_right = right.head

        while temp_left and temp_right:
            if temp_left.data < temp_right.data:
                out.append(temp_left.data)
                temp_left = temp_left.next
            else:
                out.append(temp_right.data)
                temp_right = temp_right.next
        
    # Finding last element of out
        temp_out = out.head
        while temp_out.next:
            temp_out = temp_out.next
        
        out_last = temp_out # Last element of out
    
        if not temp_left:
            out_last.next = temp_right
        else:
            out_last.next = temp_left
        return out


list1 = LinkedList()
list1.extend([5,4,1,2,7,6])
list1.print_list()
list1.merge_sort(list1.head).print_list()
