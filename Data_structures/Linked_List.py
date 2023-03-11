class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} ->', end=' ')
            temp = temp.next
        print('None')

    def insert_at_start(self, data):
        node = Node(data)
        address = self.head
        self.head = node
        node.next = address

    def insert_at_end(self, data):
        node = Node(data)
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = node
                node.next = None
            temp = temp.next

    def insert_at_node(self, data, pos):
        node = Node(data)
        pos = Node(pos)

        temp = self.head
        if temp.data == pos.data:
            self.head = node
            node.next = temp
            return None

        while temp.next.data != pos.data:
            temp = temp.next
        address = temp.next
        temp.next = node
        node.next = address

    def delete_at_start(self):
        next = self.head.next
        self.head = next


chain = Linkedlist()

chain.head = Node(1)
second = Node(2)
third = Node(3)

chain.head.next = second
second.next = third

chain.print_list()

chain.insert_at_start(0)
chain.print_list()

chain.insert_at_end(4)
chain.print_list()

chain.insert_at_node(6, 4)
chain.print_list()

chain.delete_at_start()
chain.print_list()
