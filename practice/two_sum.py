
# strategy: use a hash table to complete in O(n) time
def two_sum(int_arr, target):
    available = {}
    for i in int_arr:
        if available.get(target-i, False):
            return True
        else:
            available[i] = True
    return False
    
print( two_sum([3, 9, 13, 7],8))