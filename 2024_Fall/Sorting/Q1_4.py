# 1.4 Sorting
import random

def getInput():
    userInput = eval(input("Enter the list: "))
    print(userInput)
    return userInput

def swap(inputList,i,j):
    inputList[i],inputList[j] = inputList[j],inputList[i]

def min_index(inputList,i,j):

    minimum = inputList[i]
    minimum_index = i
    for index in range(i,j):
        if inputList[index] < minimum:
            minimum = inputList[index]
            minimum_index = index
    return minimum_index

def mySort(input_list,n):
    for i in range(0,n):
        minIndex = min_index(input_list,i,n)
        swap(input_list,i,minIndex)

    return input_list

# user_list = getInput()
user_list = random.sample(range(1, 30), 10) # random list
n = len(user_list)
print(user_list)

sorted_list = mySort(user_list,n)
print(sorted_list)
