def next_greater_element(arr):
    stack = []
    next_greater_elements = {}
    for number in arr:
        while len(stack) > 0 and stack[-1] < number:
            element = stack.pop()
            next_greater_elements[element] = number
        stack.append(number)

    for element in stack:
        next_greater_elements[element] = -1

    ret = []

    for key in next_greater_elements:
        ret.append([key,next_greater_elements[key]])
    return ret

arr = [7,2,0,1,5,4,6]
print( next_greater_element(arr) )
