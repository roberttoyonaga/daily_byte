class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # looks like a DP problem
        
        # index i reps the max $ obtainable with the last house robbed at index i
        dp = []
        
        #setup and handle small lists
        if len(nums) == 0:
            return 0
        
        dp.append(nums[0])
        
        if len(nums) == 1:
            return dp[-1]
        
        dp.append(nums[1])
        
        if len(nums) == 2:
            return max(dp[-1],dp[-2])
        
        dp.append(max(nums[2]+nums[0],nums[1]))
        
        # the meat of things
        for i in range(3, len(nums), 1):
            dp.append(max(dp[i-3],dp[i-2])+nums[i])
        
        return max(dp[len(nums)-1],dp[len(nums)-2])
        