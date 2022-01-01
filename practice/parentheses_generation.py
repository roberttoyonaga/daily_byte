#solved first try without looking at the answer :D 

def generate_parentheses(n_pairs):
    result = []
    util(0,0, n_pairs, "", result)
    return result

def util(left, right, n_pairs,current, result):
    #stopping condition
    if right == n_pairs:
        result.append(current)
    
    #recurse using depth first search
    if left < n_pairs:
        util(left + 1, right, n_pairs, current+"(", result)
    if (left - right) > 0:
        util(left, right + 1, n_pairs, current+")", result)

print(generate_parentheses(3))
