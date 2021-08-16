'''Given an array that represents different coin denominations and an amount of change you need to make, 
return the fewest number of coins it takes to make the given amount of change.
Note: If it is not possible to create the amount of change with the coins you’re given, return -1.'''

def making_change(coin_values, change_required):
    d = {0:0} # amount : min number of coins to reach that amount
    util(coin_values, change_required, 0, d)
    
    if change_required in d:
        return d[change_required]
    return -1

def util(coin_values, change_required, current_amount, d):

    # simulated choosing all possible coin values at each step
    for value in coin_values:
        new_val = current_amount + value
        
        # Stopping condition. New value is beyond the amount of change
        if new_val > change_required:
            continue

        # Cached condition. Have we already found a better solution to get to this amount?
        if new_val in d:
            if d[new_val] < d[current_amount] + 1:
                return

        # Cache the number of coins required to get to this value        
        d[new_val] = d[current_amount] + 1 

        #Recurse
        util(coin_values, change_required, new_val, d)

print(making_change([1,5, 10, 25], 78),"should print 6")
print(making_change([1,5, 10, 25], 75),"should print 3")
print(making_change([5, 10, 25], 78),"should print -1")
print(making_change([5, 20], 75),"should print 6")
