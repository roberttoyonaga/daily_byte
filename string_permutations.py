'''Given a string s consisting of only letters and digits, 
where we are allowed to transform any letter to uppercase or lowercase,
 return a list containing all possible permutations of the string.'''
 
def string_permutations(s, index, result):
    if index == len(s):
        result.append(s) # only append when we reach out stopping condition (at the leaves)
        return
    

    if not s[index].isdigit():
        string_permutations(s[:index]+s[index].lower()+s[index+1:], index + 1, result)
        string_permutations(s[:index]+s[index].upper()+s[index+1:], index + 1, result)
    else:
        string_permutations(s, index + 1, result)


r= []
string_permutations("sT9r1",0, r)
print(r)
    

