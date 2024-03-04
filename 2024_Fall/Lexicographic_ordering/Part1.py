# 1.9 Arranging String in Lexicographic Order

#   A Node class to represent a node in the linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#   A LinkedList class to maintain a linked list with lexicographic order.


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        current = self.head

        # If the list is empty or the new string comes before the head
        if self.head == None or new_data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the correct insertion position
        prev = None
        while current != None and new_data > current.data:
            prev = current
            current = current.next

        # Insert the new node after the previous node
        new_node.next = current
        prev.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} -> ', end=" ")
            temp = temp.next
        print("None")


n = int(input("Enter the number of strings: "))
linked_list = LinkedList()

for _ in range(n):
    new_string = input("Enter a string: ")
    linked_list.insert(new_string)

print("Strings in lexicographic order:")
linked_list.print_list()
