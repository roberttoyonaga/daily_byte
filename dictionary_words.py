def dictionary_words(s, d):
    dp = [False]*(len(s) + 1) #able to segment string of this length (0,i)
    dp[0] = True #account for empty string 

    for i in range(len(s)+1): #all subproblems
        for j in range(i+1): #all starting points of the substring (j,i)
            if dp[j] and (s[j:i] in d): #are we able to start from this point? is substring in dict?
                dp[i] = True
                break
    print(dp)
    return dp[-1] #return ans to final subproblem

            


print(dictionary_words("doggo", {"dog","doggo"}))
