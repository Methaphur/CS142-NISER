def subset_gen(array,weight,index = 0,subsets = []):
    if weight == 0: 
        return subsets
    
    if index >= len(array):
        return []

    # if weight < 0:
    # Back tracking shenanigans 

    include = subset_gen(array,weight-array[index],index +1,subsets +[array[index]])
    exclude = subset_gen(array,weight,index + 1,subsets)
    
    # Very janky way of dividing the subsets 
    if include:
        if exclude:
            return include,exclude
        else:
            return include
    else:
        if exclude:
            return exclude
        else:
            return []


array = [5,10,12,13,15,18]
target = 30
print(subset_gen(array,target))