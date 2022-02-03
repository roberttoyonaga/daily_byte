class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1) #use dynamic programming
        dp[0]= True
        for i in range(len(s)+1):
            for j in range(i+1): #see if there are any "break-points" we could continue from
                if dp[j] and s[j:i] in wordDict:
                    dp[i]= True
                    break
        if dp[-1]:
            return True
        
        return False