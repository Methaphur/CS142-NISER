# Part Two Rudimentary Spell Checker

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data):
        new_node = Node(new_data)
        current = self.head

        if self.head == None or new_data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        prev = None
        while current != None and new_data > current.data:
            prev = current
            current = current.next

        new_node.next = current
        prev.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} -> ', end=" ")
            temp = temp.next
        print("None")

# Introducing a notion of distance between 2 strings


def hamming_distance(string1, string2):
    if len(string1) != len(string2):
        print("Strings must be of equal length")
        return

    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1

    return distance


def find_closest_string(target, linked_list):
    current = linked_list.head
    closest = None
    min_distance = len(target)  # initializing with max possible distance
    # Move to the next node
    current = current.next
    # Iterate through the linked list
    while current != None:
        distance = hamming_distance(target, current.data)
        # If the current distance is smaller than the minimum distance, update the closest string and minimum distance
        if distance < min_distance:
            min_distance = distance
            closest = current.data
        current = current.next

    return closest


n = int(input("Enter the number of strings: "))
linked_list = LinkedList()
for _ in range(n):
    string = input("Enter the string: ")
    if len(string) != 5:
        print("String must be of length 5")
        continue
    linked_list.insert(string)

target_string = input("Enter the target string: ")
closest_string = find_closest_string(target_string, linked_list)
if closest_string:
    print(f"The closest string to {target_string} is {closest_string}")
else:
    print("No string found")
