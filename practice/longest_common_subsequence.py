'''
Idea is the 2D array represents the longest common subsequnce 
starting from idx1 in str1 and idx2 in str2
'''

def longest_common_subsequence(str1, str2):
    lcs_mat = [] #st1 rows str2 cols
    for i in range(len(str1)):
        lcs_mat.append([-1]*len(str2))

    util(str1,str2,0, 0,lcs_mat)

    print(lcs_mat)

    if lcs_mat[0][0] != -1:
        return lcs_mat[0][0]
    return 0

def util(str1, str2, idx1, idx2, lcs_mat):
    if idx1 >= len(str1) or idx2 >= len(str2): # lcs starting from beyond last element, lcs is 0
        return 0
    elif lcs_mat[idx1][idx2] != -1: #cached case
        return lcs_mat[idx1][idx2]
    
    # 3 cases: same, increasing idx1 or increasing idx2 yields longer subsequence 
    current = 0
    if str1[idx1] == str2[idx2]:
        current = 1 + util(str1, str2, idx1+1, idx2+1, lcs_mat) #same so can safely add 1 and increase both idx1 idx2
    else:
        case1 =  util(str1, str2, idx1+1, idx2, lcs_mat)
        case2 = util(str1, str2, idx1, idx2+1, lcs_mat)
        current += max(case1, case2) #which yields longer 

    lcs_mat[idx1][idx2] = current #cache result
    return current #return so outer function call can complete

print(longest_common_subsequence("abca","acea"))
