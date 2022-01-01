from collections import deque 
def sorting_func(lst):
    return lst[0]

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_intervals = sorted(intervals, key = sorting_func)
        end = -1000
        start = -1000
        merged_intervals = deque([])
        
        for interval in sorted_intervals:
            if interval[0] > end:
                merged_intervals.append([start, end])
                end = interval[1]
                start = interval[0]
            else:
                end = max(end, interval[1])
                
        merged_intervals.append([start, end])
        
        merged_intervals.popleft()
        return merged_intervals
            
                
        
        