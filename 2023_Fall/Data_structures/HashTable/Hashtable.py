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
            return f'{key} not in Hash Table'

    def delete(self,key):
        Key = self.my_hash(hash(key))
        if not self.memory[Key]:
            return
        else:
            for index,item in enumerate(self.memory[Key]):
                if item.key == key:
                    self.memory[Key].pop(index)
