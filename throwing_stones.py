import heapq
def throwing_stones(stones):
    
    while len(stones) > 1:
        heapq._heapify_max(stones)  
        stone1 = heapq._heappop_max(stones)
        stone2 = heapq._heappop_max(stones) # heappop for min heap
        
        if stone1 == stone2:
            continue
        
        stones.append(abs(stone2-stone1))
            
        
    if len(stones) ==0:
        return 0
    return stones[0]

print(throwing_stones([2, 4, 3, 8]))
# print(throwing_stones([1, 2, 3, 4]))


