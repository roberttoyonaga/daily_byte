def edit_distance(s1, s2):
    dp = []
    for row in range(len(s1)):  
        dp.append([0]*len(s2))
    
    for l1 in range(len(s1)):
        for l2 in range(len(s2)):
            if l1 == 0: #empty string
                dp[l1][l2] = l2
            elif l2 == 0:
                dp[l1][l2] = l1
            elif s1[l1-1] == s2[l2-1]: #char are the same
                dp[l1][l2] = dp[l1-1][l2-1] #becauase we choose to index from 1
            else:                     #replace         Insert        remove
                dp[l1][l2] = 1 + min( dp[l1-1][l2-1], dp[l1][l2-1], dp[l1-1][l2] )
    print(dp)
    return dp[len(s1)-1][len(s2)-1]
print(edit_distance("aat","baat"))
