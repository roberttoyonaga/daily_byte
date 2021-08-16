def popsical_stand(customers):
    fives = 0
    tens = 0 
    twenties = 0

    for customer in customers:
        if customer == 5:
            fives +=1
        elif customer == 10:
            tens +=1
        elif customer ==20:
            twenties +=1
        
        change = customer - 5 
        if change == 0:
            continue
        elif change == 5 and fives > 0:
            fives -= 1
        elif change == 15 and (fives > 0 and tens > 0 ): #always give away largest bill first so we have the most flexibility
            fives -=1
            tens -=1
        elif change == 15 and (fives > 2):
            fives -=3
        else:
            return False
    return True

print(popsical_stand([5,5,5,20])) 



