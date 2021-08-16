

def longest_increasing_subsequence(nums):
    #This array is the longest subsequence with each element as the END of the subsequence
    dp = [1]*len(nums) # longest subsequence must be at least 1

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]: #if greater, we're appending to the subsequence that ends at nums[j]
                dp[i] = max(dp[i], dp[j] + 1 )
    print(dp)
    return max(dp)


print(longest_increasing_subsequence([1, 9, 7, 4, 7, 13,2,222]))
            