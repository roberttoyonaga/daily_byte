# sept 25 2021
from collections import deque

def distance_to_rabbit_holes(arr):
    ret = []
    rows = len(arr)
    cols = len(arr[0])
    for row in range(rows):
        ret.append([])
        for col in range(cols):
            if arr[row][col]==1:
                ret[-1].append(bfs(arr, rows,cols, row, col)) #run bfs whenever we find a rabbit to find closest hole
            else:
                ret[-1].append(arr[row][col])
    return ret

def is_valid_move(arr, row, col, visited): #helper
    if row < 0:
        return False
    elif row >= len(arr):
        return False
    elif col < 0:
        return False
    elif col >= len(arr[0]):
        return False
    elif arr[row][col] == -1:
        return False
    elif visited[row][col]:
        return False
    else:
        return True

def try_visit_node(queue, arr, visited, row, col): #helper
    if is_valid_move(arr, row,col, visited):
            queue.append((row, col))
            visited[row][col] = True
            if arr[row][col] == 0:
                return True
    return False

def bfs(arr, rows, cols, row, col): #bfs because we want shortest path
    visited = []
    for i in range(rows):
        visited.append([False]*cols)

    queue = deque([])
    visited[row][col] = True
    queue.append( (row,col) )

    count = 0
    while queue:
        count +=1
        size = len(queue) # need this because we want to calculate distance (count number of levels)
        for i in range(size):
            i,j = queue.popleft()
            if try_visit_node(queue,arr,visited, i, j+1) or try_visit_node(queue,arr,visited, i+1, j) or try_visit_node(queue,arr,visited, i, j-1) or try_visit_node(queue,arr,visited, i-1, j):
                return count


test_arr = [[1, 1, 1], [1, -1, -1], [1,  1,  0]]   
print(distance_to_rabbit_holes(test_arr))
test_arr_2 = [[-1, 0, 1], [1, 1, -1], [1,  1,  0]]   
print(distance_to_rabbit_holes(test_arr_2))