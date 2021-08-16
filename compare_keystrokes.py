def compare_keystrokes(s,t):
    s_parsed = parse_keystrokes(s)
    t_parsed = parse_keystrokes(t)
    if len(s_parsed) != len(t_parsed):
        return False
    for i in range(len(s_parsed)):
        if s_parsed[i] != t_parsed[i]:
            return False
    return True

def parse_keystrokes(str):
    parsed = []
    for char in str:
        if char != "#":
            parsed.append(char)
        elif len(parsed)!=0:
            parsed.pop()
    return parsed
    
print(compare_keystrokes("como#pur#ter","computer"))
print(compare_keystrokes("cof#dim#ng","code"))
print(compare_keystrokes("ABC#","CD##AB"))