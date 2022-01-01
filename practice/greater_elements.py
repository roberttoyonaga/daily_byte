def greater_elements(l1, l2):
    # this only works if the numbers are unique
    
    mapping = {}
    ret = []
    for i in range(len(l1)):
        mapping[l1[i]] = i
        ret.append(l1[i])

    l1.sort()
    l2.sort()
    
    i1 = 0
    i2 = 0
    while i1<len(l1):
        if i2>=len(l2):
            ret[ mapping[l1[i1]] ] = -1
            i1 += 1
            continue

        if l1[i1]>=l2[i2]:
            i2 +=1
            continue
        ret[mapping[l1[i1]]] = l2[i2]
        i1 += 1
    return ret

print(greater_elements([2,4,100,3,1],[1,2,3,4]))
