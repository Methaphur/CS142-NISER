# Question 1
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

        if self.head is None:
            self.head = new_node
            return 

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
        if self.head is None: 
            return 

        current = self.head
        self.head = current.next


    def delete_at_end(self):
        if self.head is None: 
            return 

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

print("Qs 1.")
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


print("Qs 2. Palindrome check")

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
    

    def append(self,alpha): 
        new_node = Node(alpha)
        
        if self.head is None:
            self.head = new_node
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
    
    def extend(self,data): 
        for data in data:
            self.append(data) 


    def find_middle(self,head): 
        if head is None: 
            return head
        
        slow_node = head 
        fast_node = head  
        
        while fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return slow_node
            
            

    def reverse_list(self,head):
        current = head
        prev = None

        while current is not None:
            next = current.next 
            current.next = prev 
            prev = current
            current = next
        head = prev
        return head
    
    
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
                mid = prev_slow.next 
                slow_node = slow_node.next

            remaining_list = slow_node

            prev_slow.next = None 

            remaining_list = self.reverse_list(remaining_list)
            output_Bool = self.compare_lists(head,remaining_list)  


            remaining_list = self.reverse_list(remaining_list)
            if mid: 
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


print('Qs 3.a Insertion Sort')
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    node = self.head
    while node:
      print(f'{node.data} -> ', end='')
      node = node.next
    print(None)
  
  def append(self,data):
    node = Node(data)
    temp = self.head
    if not temp:
      self.head = node

    while temp:
      if temp.next is None:
        temp.next = node
        node.next = None
      temp = temp.next

  def extend(self,data):
    for i in data:
        self.append(i)

  def insert_into_sorted_list(self, sorted, node):
    head = sorted.head

    if not head: 
      sorted.append(node.data)
      return sorted

    prev = None
    while head:
      if head.data >= node.data:

        if prev:
          prev.next = node
        else:
          sorted.head = node

        node.next = head
        return sorted

      prev = head
      head = head.next


    sorted.append(node.data)
    return sorted

  def insertion_sort(self):

    sorted = LinkedList()
    head = self.head
    
    while head:
      next = head.next
      sorted = self.insert_into_sorted_list(sorted, head)
      head = next

    return sorted

list1 = LinkedList()
list1.extend([1,3,2,6,7,8,4])
list1.print_list()
list1 = list1.insertion_sort()
list1.print_list()
print()


print("Qs 3.b Merge Sort ")
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
    

    def append(self,alpha): 
        new_node = Node(alpha)
        
        if self.head is None:
            self.head = new_node
            return 
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
    
    def extend(self,data):
        for data in data:
            self.append(data)

    def find_middle(self,head): 
        if head is None: 
            return head
        
        slow_node = head 
        fast_node = head 
        
        while fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        
        return slow_node

   
    def merge_sort(self,head):
    
        if head.next is None:
            out = LinkedList()
            out.append(head.data)
            return out

        mid = self.find_middle(head) 
        mid_next = mid.next          
        mid.next = None
    
        left_list = self.merge_sort(head)
        right_list = self.merge_sort(mid_next)

        return self.merge(left_list,right_list)


    def merge(self,left,right):
        out = LinkedList() 

        temp_left = left.head
        temp_right = right.head

        while temp_left and temp_right:
            if temp_left.data < temp_right.data:
                out.append(temp_left.data)
                temp_left = temp_left.next
            else:
                out.append(temp_right.data)
                temp_right = temp_right.next
        
        temp_out = out.head
        while temp_out.next:
            temp_out = temp_out.next
        
        out_last = temp_out
    
        if not temp_left:
            out_last.next = temp_right
        else:
            out_last.next = temp_left
        return out


list1 = LinkedList()
list1.extend([5,4,1,2,7,6])
list1.print_list()
list1.merge_sort(list1.head).print_list()
