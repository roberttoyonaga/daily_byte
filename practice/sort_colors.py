class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # in place means constant memory, cant use another data structure like hashmap etc.
        start = 0
        end = len(nums) - 1
        i = start
        while i <= end:
            if nums[i] == 0:
                # swap with start
                temp = nums[start]
                nums[start] = nums[i]
                nums[i] = temp
                start += 1
                i += 1 # don't need to re-evalutate this index
            elif nums[i] == 1:
                # dont need to do any swap
                i += 1 # don't need to re-evalutate this index
            elif nums[i] == 2:
                temp = nums[end]
                nums[end] = nums[i]
                nums[i] = temp
                end -= 1
            
        return nums