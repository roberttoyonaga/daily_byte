class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        for num in nums_set:
            #are we at the start of the sequence?
            curr_max = 0
            if num-1 not in nums_set:
                curr_max += 1
                curr_num = num + 1
                while curr_num in nums_set:
                    curr_max +=1
                    curr_num +=1
                
            ret = max (ret, curr_max)
        return ret