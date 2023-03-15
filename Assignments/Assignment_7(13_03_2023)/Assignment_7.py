'''
Qs1. Create a singly linked list with insert and delete operations at the beginning
and at the end where each node contains an alphabet and a number as data.
'''
print("Qs 1 Insertion and Deletion")
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
print()

'''
Qs 2. Check if the alphabets in the linked list from left to right induce a palindrome
or not in O(n) time where n is the length of the linked list.
'''
print("Qs 2 Palindrome check")
# Approach 3: What we are expected to use 
# This approach does not use a separate array / linked list 

print("Approach 1: ")
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


    def find_middle(self,head): 
        if head is None: # Empty linked list
            return head
        
        slow_node = head # Traverses one node at a time 
        fast_node = head # Traverses two nodes at a time 
        
        while fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return slow_node
            
            
    # Accepts a node and reverses the linked list from that node and returns the current head
    def reverse_list(self,head):
        current = head
        prev = None

        while current is not None:
            next = current.next # Storing the next node in next
            current.next = prev 
            prev = current
            current = next
        head = prev
        return head
    
    # Accepts whether a linked list from a given node is a palindrome
    def isPalindrome(self, head):

        slow_node = head
        fast_node = head
        prev_slow = head

        mid = None

        if head is not None and head.next is not None:

            while fast_node and fast_node.next:

                fast_node = fast_node.next.next
                prev_slow = slow_node
                slow_node = slow_node.next


            if fast_node is not None:
                mid = prev_slow.next # only stored for reconstructing our linked list
                slow_node = slow_node.next

            remaining_list = slow_node

            prev_slow.next = None # First half is over 

            remaining_list = self.reverse_list(remaining_list)
            output_Bool = self.compare_lists(head,remaining_list)  


        # Reconstructing Original Linked list
            remaining_list = self.reverse_list(remaining_list)
            if mid: # There was a mid node (odd number of nodes)
                prev_slow.next = mid
                mid.next = remaining_list

            else:
                prev_slow.next = remaining_list
        return output_Bool


    def compare_lists(self,head1,head2):
        temp1 = head1
        temp2 = head2

        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        
        if temp1 is None and temp2 is None:
            return True
        
        else:
            return False


list1 = LinkedList()
list1.extend(['C','S','1','4','2'])
list1.print_list()
print(list1.isPalindrome(list1.head))


list2 = LinkedList()
list2.extend(['r','a','c','e','c','a','r'])
list2.print_list()
print(list2.isPalindrome(list2.head))
print()


# Approach 2: Using a temporary array 
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
            
    def is_palindrome(self): # Using a temp array to store data 
        check = []
        temp = self.head
        while temp:
            check.append(temp.data)
            temp = temp.next
        
        if check == list(reversed(check)):
        # if check == check[::-1]: (list slicing method)
            # print('Is a palindrome')
            return True

        # print('Not a palindrome')
        return False

print("Approach 2: ")
list1 = LinkedList()
list1.extend(['r','a','c','e','c','a','r',]) # Palindrome Linked list
list1.print_list()
print(list1.is_palindrome())

list2 = LinkedList()
list2.extend(['M','e','t','h','a','p','h','u','r']) # Not a palindrome
list2.print_list()
print(list2.is_palindrome())
print()

# Approach 2: Reversing linked list and traversing both again
print("Approach 3: ")
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

    def insert_at_start(self,data):
        new_node = Node(data)

        current = self.head 
        self.head = new_node
        new_node.next = current

    def reverse_list(self):
        reverse_list = LinkedList()

        temp = self.head
        while temp:
            reverse_list.insert_at_start(temp.data)
            temp = temp.next
        return reverse_list


    def is_palindrome(self):
        reverse = self.reverse_list()

        temp = self.head
        r_temp = reverse.head
        while temp:
            if temp.data == r_temp.data:
                temp = temp.next
                r_temp = r_temp.next
            else:
                return False
        
        return True


list1 = LinkedList()
list1.extend(['r','a','c','e','c','a','r',]) # Palindrome Linked list
list1.print_list()
print(list1.is_palindrome())

list2 = LinkedList()
list2.extend(['M','e','t','h','a','p','h','u','r']) # Not a palindrome
list2.print_list()
print(list2.is_palindrome())
print()

'''
Rearrange the nodes (links between them) to sort the linked list (based on the
number data) using (a) insertion sort sort algorithm, (b) merge sort algorithm.
'''

print("Qs 3.b Merge Sort for Linked Lists")
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
