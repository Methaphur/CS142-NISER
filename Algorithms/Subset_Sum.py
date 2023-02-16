def subset_sum(arr, target):
    arr.sort() # Sorting the array so that weight gradually increases
    def is_subset_sum(current, weight, current_subset):
        # If sum has gone past the target element : skip
        if weight + arr[current] > target: 
            return False  
        
        # If the sum till current element is target 
        elif weight + arr[current] == target:   
            return True

        # Current has gone through all the elements in the list
        # Still no such sum pair has been found 
        if current == len(arr) - 1:
            return False
        
        else:
        # We call the subset function twice , once where we include the current element in the sum
        # And one where we exclude the current element in the sum
          include = is_subset_sum(current+1, weight + arr[current], current_subset + [arr[current]]) 
          exclude = is_subset_sum(current+1, weight, current_subset)

          return  include or exclude
    
    return is_subset_sum(0, 0, [])

input = [2,3,5,12,15]
target = 27
print(f'Input = {input} target = {target}')
print(subset_sum(input,target))