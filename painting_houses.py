''''
Recursive solution with no memoization Top Down
'''
def painting_houses(colors):
    color = colors[0].index(min(colors[0]))
    return util(colors, 1, color) + colors[0][color]
    
def util(colors, i, last_color):
    if i==len(colors) -1 :
        return min(colors[i])

    if last_color==0:
        color = colors[i].index(min(colors[i][1],colors[i][2])) #WRONG you can't just greedily choose the cheapest!
    elif last_color==1:
        color = colors[i].index(min(colors[i][0],colors[i][2]))
    if last_color==2:
        color = colors[i].index(min(colors[i][0],colors[i][1]))

    return util(colors, i+1 , color) + colors[i][color]

print(painting_houses([[1, 3, 5],[2, 4, 6],[5, 4, 3]]),8)
print(painting_houses([[14,2,11],[11,14,5],[14,3,10]]),10)
print(painting_houses([[1,2,3],[1,4,6]]),3)

'''
dp solution Bottom Up
'''


def painting_houses_dp(colors):
    #Reuse the colors array
    
    '''
    Simulate choosing all three possible choices (solves the problem with the greedy approach above)
    We know that there is only one way to make each choice (add on min of 2 available previous choices) 
     '''
    for i in range(1, len(colors), 1):
        colors[i][0] += min(colors[i-1][1],colors[i-1][2]) 
        colors[i][1] += min(colors[i-1][0],colors[i-1][2]) 
        colors[i][2] += min(colors[i-1][0],colors[i-1][1])   

    return min(colors[-1])


print("\nDP solution:")
print(painting_houses_dp([[1, 3, 5],[2, 4, 6],[5, 4, 3]]),8)
print(painting_houses_dp([[14,2,11],[11,14,5],[14,3,10]]),10)
print(painting_houses_dp([[1,2,3],[1,4,6]]),3)