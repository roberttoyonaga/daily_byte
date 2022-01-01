class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #log(n) means binary search
        # determine if rotated by checking the ends of the array (left ,right)
        # if not rotated, then normal binary search
        # if rotated, we need to find the pivot point using binary serach
            # move right if mid > right, move left if mid < left
        # once pivot is found, then do binary search from pivot to either end

        pass