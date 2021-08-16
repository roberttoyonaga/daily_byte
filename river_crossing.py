'''A frog is attempting to cross a river to reach the other side. Within the river, 
there are stones located at different positions given by a stones array (this array is in sorted order). 
Starting on the first stone (i.e. stones[0]), the frog makes a jump of size one potentially
 landing on the next stone. If the frog’s last jump was of size x, the frog’s next jump may be of 
 size x - 1, x, or x + 1. Given these following conditions return whether or not the frog can reach 
 the other side.
Note: The frog may only jump in the forward direction.
 '''
def river_crossing(stones):
    jump_size = 1
    last_stone = 0
    success = True
    for stone in stones:
        distance = stone - last_stone
        if (jump_size-1) > distance or (jump_size + 1) < distance:
            print(jump_size, distance,stone, last_stone)
            success = False
            break
        last_stone = stone
        jump_size = distance
    return success

print(river_crossing([0, 1, 2, 4,7]))
print(river_crossing([0, 1, 1, 2,3,4]))