def longest_common_prefix(str_arr):
    #longest prefix can only be length of shortest string
    #get length of shortest string
    shortest_len = 10000000
    shortest_word= ""
    for s in str_arr:
        if len(s)<shortest_len:
            shortest_len = len(s)
            shortest_word = s

    lcp = ""

    for i in range(len(shortest_word)):

        letter = shortest_word[i]
        all_shared = True

        for s in str_arr:
            if letter is not s[i]:
                all_shared = False
                break
    
        if all_shared:
            lcp += letter
    return lcp            
print( longest_common_prefix(["spot", "spotty", "spotted"]) )