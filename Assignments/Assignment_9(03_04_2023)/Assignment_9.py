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
        self.memory[key].append(item)

    def search(self,key):
        Key = self.my_hash(hash(key))
        if not (self.memory[Key]):
            return f'{key} not in Hash Table'
        
        else:
            for i in self.memory[Key]:
                if i.key == key:
                    return i.value

    def delete(self,key):
        Key = self.my_hash(hash(key))
        if not self.memory[Key]:
            return
        else:
            for index,item in enumerate(self.memory[Key]):
                if item.key == key:
                    self.memory[Key].pop(index)
                    
print("Qs 1.")
st1 = Item("John",12)
st2 = Item("Doe",13)
st3 = Item("Doe",15)

table = HashTable(10)
for i in [st1,st2,st3]:
    table.insert(i)

print(f'John: {table.search("John")}')
print()
print("Qs 2.")
table = HashTable(10)
print("\nItem Insertion")
print(f'ILY: {table.search("ILY")}')

table.insert(Item("Methaphur" ,69))
table.insert(Item("ILY",143))
table.insert(Item("Amongus",8055))

print("After Insertion")
print(f'ILY: {table.search("ILY")}')

print("\nItem Search")
print(f'ILY: {table.search("ILY")}')

print("\nItem Deletion")
print(f'Methaphur: {table.search("Methaphur")}')
print("After Deletion")
table.delete("Methaphur")
print(f'Methaphur: {table.search("Methaphur")}')
