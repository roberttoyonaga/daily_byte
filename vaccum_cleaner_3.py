def vaccum(str):
    horiz_dir = 0
    vert_dir = 0
    for letter in str:
        if letter  == "U":
            vert_dir += 1
        elif letter == "D":
            vert_dir -= 1
        elif letter == "R":
            horiz_dir +=1
        elif letter == "L":
            horiz_dir -=1
    if vert_dir == 0 and horiz_dir == 0:
        return True
    else:
        return False

print("LR", vaccum("LR"))
print("URURD", vaccum("URURD"))
print("RUULLDRD", vaccum("RUULLDRD"))