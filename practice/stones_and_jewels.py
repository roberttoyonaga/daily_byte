''' 
I can think of two ways to do this
1) hash table is O(n), sacrifice space
2) sort stones and sort jewels and keep a counter for each list (s, j)  as you step through them. 
If sorting is done in-place then it is dependent on sortign speed. No additional space neededs
'''

def stones_and_jewels(stones, jewels):
    stone_dict = {}
    count =0 

    for stone in stones:
        stone_dict[stone] = True

    for jewel in jewels:
        if stone_dict.get(jewel, False):
            count+=1

    return count

print(stones_and_jewels("aBaa","aabB"))
 