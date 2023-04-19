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
print()

list2 = LinkedList()
list2.extend(['r','a','c','e','c','a','r'])
list1.print_list()
print(list2.isPalindrome(list2.head))
