def correct_capitalization(str):
    #checks if capitalization is used correctly
    first_cap = False
    other_cap = False
    lower = False

    if str[0].isupper():
        first_cap = True

    for i in range(1, len(str)):
        if str[i].isupper():
            other_cap =True
        else:
            lower = True

    #all caps
    if first_cap == True and lower == False:
        return True
    #all lower
    elif first_cap == False and other_cap == False:
        return True
    #cap at front
    elif first_cap == True and other_cap == False:
        return True
    else:
        return False

print(correct_capitalization("USA"),correct_capitalization("Calvin"), correct_capitalization("coding"),correct_capitalization("compUter"), correct_capitalization("CompUter"))
