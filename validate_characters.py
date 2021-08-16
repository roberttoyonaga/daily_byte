def matches(r,l):
    if r == "{" and l == "}":
        return True
    elif r == "(" and l == ")":
        return True
    elif r == "[" and l == "]":
        return True
    return False

def validate_characters(s):
    #use a list as a stack 
    stack = []
    pop = {'}', ']', ')'}
    push = {'{', '[', '('}

    for char in s:
        if char in push:
            stack.append(char)
        if char in pop:
            backOfStack = stack.pop()
            if not matches(backOfStack, char):
                return False
        
    if len(stack) != 0:
        return False
    return True

print(validate_characters('({{[]}()})'))