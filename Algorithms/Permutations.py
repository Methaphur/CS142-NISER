def permute(string):
    permutations= []
    def _permute(string,out):
        # If length of string is 0 , Out will have one permuations
        if not len(string):
            permutations.append(out) 

        # Iterating through all the elements in list and permuting with the rest
        for index,item in enumerate(string):
           _permute(string[:index] + string[index+1:], out + item)

    _permute(string,"")
    return permutations
    

string = input('Enter string to be permuted: ')
permutations = permute(string)
print(f'Total permutations = {len(permutations)}')
print(permutations)
