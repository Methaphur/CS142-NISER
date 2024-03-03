def subset_sum(arr,target,length): # Wrapper function
    def _subset_sum(subsets,curr): 
        if curr == len(arr):       # Iterating through all elements in list
            return None
        
        if sum(subsets) > target:  # If subset sum > target : skip
            return None 
    
        if sum(subsets) == target and len(subsets) == length:
            print(subsets)         # Requires subset sum condition

        _subset_sum(subsets+[arr[curr]],curr+1)  # Including current element
        _subset_sum(subsets,curr+1)              # Excluding current element
    
    _subset_sum([],0)              # Callign function with empty subset and starting curr 0 

list1 = [3,34,4,12,5,2]
target = 9
k = 2 
print(f'Input = {list1} target = {target} length = {k}')
subset_sum(list1,target,k)
