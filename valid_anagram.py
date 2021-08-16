def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    s_letters= {}

    for letter in s: 
        if s_letters.get(letter, False):
            s_letters[letter] += 1
        else:
            s_letters[letter] = 1

    for letter in t:
        if s_letters.get(letter, False):
            if s_letters[letter] > 0:
                s_letters[letter] -= 1 
            else:
                print("false1")
                return False
        else:
            print("false2")

            return False

    return True
print(valid_anagram("listen","silenn"))