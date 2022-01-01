class Solution(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        # try greedy approach with 2 pointers
        max_water = 0
        start = 0
        end = len(heights)-1
        
        while start < end:
            current_capacity = (end-start)*min(heights[start],heights[end])
            if current_capacity > max_water:
                max_water = current_capacity
                
            #advance the pointer that points to the smaller line
            if heights[start] < heights[end]:
                start +=1
            else: 
                end -=1
        return max_water
        