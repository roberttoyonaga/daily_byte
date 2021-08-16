'''Given a staircase where the ith step has a non-negative cost associated with it given by cost[i], 
return the minimum cost of climbing to the top of the staircase.
 You may climb one or two steps at a time and you may start climbing from either the first or second step. 

This is a memoization problem. 
 '''

def stairmaster(stairs):
    costs = [0]*len(stairs) # the cost to get to the top of the stairs from the current step
    util(stairs, 0, costs)
    util(stairs, 1, costs)

    if costs[0] < costs[1]:
        return costs[0]
    return costs[1]


def util(stairs, step, costs):
    if step >= len(stairs):
        return 0 #don't add anything
    if costs[step] != 0:
        return costs[step] #this has been cached

    #recursion
    #we know that there are two recursive calls because there are two options at each step
    single =  util(stairs, step+1, costs ) #what is the cost from this step
    double = util(stairs, step+2, costs)

    #update costs
    if single < double: 
        costs[step] = single + stairs[step]
    else: 
        costs[step] = double + stairs[step]

    #return 
    return costs[step]

print(stairmaster([5, 10, 20,1 ,3,22])) #14
print(stairmaster([1, 5, 10, 3, 7, 2])) #10
print(stairmaster([5, 10, 2,1 ,3,22])) #10
print(stairmaster([5, 10, 2,1 ,3,22,100])) #30
print(stairmaster([5, 10, 2])) #7

