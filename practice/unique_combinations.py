'''
the "start" variable ensures uniqueness. For example, only the very 
first path throught the recursive tree will select always the first element of the nums list.
This is because start will be 0 for each successive recursive call.
'''

def unique_combinations(nums, target):
    result = []
    util(nums, [], result,target,0)
    return result
def util(nums, current, result, remaining, start):
    if remaining < 0:
        return
    elif remaining == 0:
        result.append(current)
    
    while start < len(nums):
        copy = list(current) # need to deep copy
        copy.append(nums[start])
        util(nums, copy, result, remaining - nums[start], start)

        start +=1 

print(unique_combinations([2,4,6,3], 6))