def uncommon_words(sentence1, sentence2):
    # this solution takes O(n) time excluding sorting. 
    # Including sorting, it will depend on how fast the sorting is
    
    #tokenize
    split1 = sentence1.split()
    split2 = sentence2.split()
    
    #sort
    split1.sort()
    split2.sort()

    #keep counters as you go through each word
    count1 = len(split1) - 1
    count2 = len(split2) - 1

    uncommon = []

    while count1 > 0  or count2 > 0:
        print(count1, count2)
        if split2[count2] == split1[count1]:
            count1 -= 1
            count2 -=1
            continue

        if split2[count2] > split1[count1]:
            uncommon.append(split2[count2])
            count2 -= 1
        elif split2[count2] < split1[count1]:
            uncommon.append(split1[count1])
            count1 -= 1
        else:
            uncommon.append(split2[count2])
            uncommon.append(split1[count1])
            count1 -= 1
            count2 -=1

    return uncommon


print(uncommon_words("copper coffee pot", "hot coffee pot"))
#print(uncommon_words("a e d  bb", "a b bb c"))
