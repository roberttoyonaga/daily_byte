"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        success = [False]*length
        for i in range(length):
            index = length - i - 1
            if index == length -1: #base case
                success[index] = True
            elif nums[index] != 0:
                for j in range(nums[index]): # see if any reachable elements are able to reach the end
                    jump_size = j+1  # dont start at 0
                    if success[index + jump_size]:
                        success[index] = True #if so, you can reach the end from your position
                        break
        print(success)
        return success[0]
        