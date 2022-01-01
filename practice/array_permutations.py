import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.util(ret,[], nums)
        return ret
    def util(self,ret, curr, nums):
        if not nums:
            ret.append(curr)
            return
        
        #try taking each of the positions
        for i in range(len(nums)):
            curr_copy = copy.deepcopy(curr)
            curr_copy.append(nums[i])
            nums_copy = copy.deepcopy(nums)
            del nums_copy[i]
            self.util(ret, curr_copy, nums_copy)
            