class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node_value):
        node = Node(node_value)
        node.next = self.head
        self.head = node

    def print_list(self):
        temp = self.head
        while temp is not None:  # convention to use is not None instead of != None
            print(f'{temp.value} -> ', end='')
            temp = temp.next
        print('None')

    def removeFirst(self):
        self.head = self.head.next

    def findith(self, n): # Search for the nth element in the list
        temp = self.head
        i = 0
        while i < n:
            temp = temp.next
            i += 1
        return temp

    def remove_ith(self, i):
        if i == 0:
            self.removeFirst()
            return
        temp = self.findith(i - 1)
        temp.next = temp.next.next

    def insert_ith(self, i, value):
        if i == 0:
            self.add(value)
            return
        temp = self.findith(i - 1)
        node = Node(value)
        node.next = temp.next
        temp.next = node
    
    # Search for a value in the list
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

list1 = LinkedList()
list1.add(5)
list1.add(4)
list1.add(3)
list1.add(6)

list1.print_list()
list1.removeFirst()
list1.print_list()
list1.add(1)
list1.print_list()
list1.remove_ith(2)
list1.print_list()
list1.insert_ith(3, "string")
list1.print_list()
list1.insert_ith(4, "new")
list1.print_list()
list1.insert_ith(0, "test")
list1.print_list()
list1.remove_ith(0)
list1.print_list()
print(list1.search(3))