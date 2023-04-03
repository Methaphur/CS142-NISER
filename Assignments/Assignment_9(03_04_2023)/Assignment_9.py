class Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value 
    
    def hash(self):
        return hash(self.key)

class HashTable:
    def __init__(self,table_size):
        self.memory = [[] for i in range(table_size)]        

    def my_hash(self,key): # Modulo func
        return key%len(self.memory)

    def insert(self,item):
        key = self.my_hash(item.hash())
        if not self.memory[key]:
            self.memory[key] = item
        else:
            temp = self.memory[key] 
            self.memory[key] = LinkedList()
            self.memory[key].add(temp)
            self.memory[key].add(item)

    def Search(self,key):
        Key = self.my_hash(hash(key))

        if not type(self.memory[Key]) == LinkedList:
            return self.memory[Key].value  
        else:
            return self.memory[Key].Search(key)        

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

    def Search(self,key):      
        current = self.head
        while current:
            if current.data.key == key:
                return current.data.value
            current = current.next

print("Qs 1. ")
st1 = Item("John",12)
st2 = Item("Doe",13)
st3 = Item("Doe",15)

table = HashTable(10)
for i in [st1,st2,st3]:
    table.insert(i)

print(f'John: {table.Search("John")}')



class Item:
    def __init__(self,key,value):
        self.key = key
        self.value = value 
    
    def hash(self):
        return hash(self.key)

class HashTable:
    def __init__(self,table_size):
        self.memory = [[] for i in range(table_size)]        

    def my_hash(self,key): # Modulo func
        return key%len(self.memory)

    def insert(self,item):
        key = self.my_hash(item.hash())
        if not self.memory[key]:
            self.memory[key] = item
        else:
            temp = self.memory[key] 
            self.memory[key] = LinkedList()
            self.memory[key].add(temp)
            self.memory[key].add(item)

    def Search(self,key):
        Key = self.my_hash(hash(key))
        if self.memory[Key]:
            if type(self.memory[Key]) != LinkedList:
                if self.memory[Key].key == key:
                    return self.memory[Key].value
                else:
                    return (f"{key} not in Hash table")

            else:
                search = self.memory[Key].Search(key)
                if search:
                    return search
        else:
            return (f"{key} not in Hash table")
    

    def Delete(self,key):   
        Key = self.my_hash(hash(key))

        if not type(self.memory[Key]) == LinkedList:
            self.memory[Key] = []
        else:
            self.memory[Key].Delete(key)
        
        
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

    def Search(self,key):      
        current = self.head
        while current:
            if current.data.key == key:
                return current.data.value
            current = current.next
        return False

    def Delete(self,key):
        current = self.head
        # key in head
        if current.data.key == key:
            self.head = current.next
            return
        
        # Iterating through nodes until key
        while current.next:
            if current.next.data.key == key:
                if current.next.next:  
                    current.next = current.next.next
                else:  
                    current.next = None # Key in last node
                    return
            current = current.next

    def printlist(self):
        curr = self.head
        while curr:
            print(f'{curr.data.key} ->',end=" ")
            curr = curr.next
        print("None")
print()

table = HashTable(10)
items = {"John" : 120, "Methaphur" : 141, "ILY" :143}
for i,j in items.items():
    table.insert(Item(i,j))

print("Qs 2.")
print('Item Search: ')
print(f'Methaphur: {table.Search("Methaphur")}')

print('\nInsert Item: ')
print(table.Search("SweepingBishops"))

print("\nAfter Insertion: ")
table.insert(Item("SweepingBishops",6.626))
print(f'SweepingBishops: {table.Search("SweepingBishops")}')

print("\nItem Deletion: ")
print(f'John: {table.Search("John")}')
table.Delete("John")
print(f'John: {table.Search("John")}')
