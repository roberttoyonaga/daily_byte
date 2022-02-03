'''The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container.
 If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
 '''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        [e,b,d,c,a] [e,c,a,b,d]    
        Use notion of a pivot
        
        #solved in 43 minutes, no hints
        """
        finished = False
        popped_nums = [] #set of all the numbers we allowed to rearrange
        prev_num = -1
        for i in range(len(nums)-1,-1,-1):#go from back to front
            popped_nums.append(nums[i])#add to the list as we go 
            
            if nums[i] < prev_num:
                popped_nums.sort()
                print("pivot:", nums[i])
                
                #find next highest number from pivot
                for j in range(len(popped_nums)):
                    if popped_nums[j] > nums[i]:
                        nums[i] = popped_nums.pop(j)
                        print("next highest:", nums[i])
                        break
                        
                #add the popped numbers back to the original arr in ascending order
                j =0 
                start = len(nums) - len(popped_nums)
                while j<len(popped_nums):
                    nums[start+j] = popped_nums[j]
                    j+=1
                    
                finished = True
                break
                
            else:
                prev_num = nums[i]
        if not finished:
            nums.reverse()