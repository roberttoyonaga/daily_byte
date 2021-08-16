def palindrome_splitting(s):
    results = []
    util(s,[], results, 0)
    return results

def util(s, current, results, start):
    #stopping condition
    if start == len(s):
        results.append(current)
    i = start
    while i < len(s):
        if isPalindrome(s, start, i):
            copy = list(current)
            copy.append(s[start:i+1])
            util(s, copy, results, i+1)
        i += 1 


def isPalindrome(p, i, j):
    while i<j:
        if p[i] != p[j]:
            return False
        i += 1
        j -=1
    return True

print(palindrome_splitting("abcba"))
