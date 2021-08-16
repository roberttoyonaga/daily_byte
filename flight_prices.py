'''
A company is booking flights to send its employees to its two satellite offices A and B.
The cost of sending the ith employee to office A and office B is given by prices[i][0] and prices[i][1] respectively.
Given that half the employees must be sent to office A and half the employees must be sent to office B,
return the minimum cost the company must pay for all their employees’ flights.

Steps I took:
    1. On the first pass, assign each employee to the office that is cheapest for them to fly to (ideal choice)
    2. Find the office that has too many employees
    3. Sort employees at that office by the cost of switching flights (not the cost of the flight itself)
    4. Switch flights until the offices have an equal number of employees

Proper solution:
    1. sort by diff / how much you save by flying to office A (could be negative). 
    2. send the first half of the sorted employees to office A
'''

from functools import cmp_to_key
DEBUG = False

def compareA(item1, item2):
    if (item1[1] - item1[0]) < (item2[1] - item2[0]): # Sort by how much switching flights would increase the sum (not by the absolute val of the new cost)
        return -1
    elif (item1[1] - item1[0]) > (item2[1] - item2[0]):
        return 1
    else:
        return 0

def compareB(item1, item2):
    if (item1[0] - item1[1]) < (item2[0] - item2[1]):
        return -1
    elif (item1[0] - item1[1]) > (item2[0] - item2[1]):
        return 1
    else:
        return 0

def flight_prices(prices):
    #first pass assign each employee to the cheapest option
    officeA = []
    officeB = []
    for price in prices:
        if price[0] < price[1]:
            officeA.append(price)
        else:
            officeB.append(price)
    if DEBUG:
        print("before balance",officeA, officeB) 
    
    #balance the flights to each office
    if len(officeA) > len(officeB):
        officeA.sort(key=cmp_to_key(compareA))  #custom comparator for the sorting
        while len(officeA) != len(officeB):         # need to make them even lengths
            officeB.append(officeA.pop(0))

    else:
        officeB.sort(key=cmp_to_key(compareB))
        while len(officeA) != len(officeB):
            officeA.append(officeB.pop(0))

    if DEBUG:
        if len(officeA) != len(officeB):
            print("ERROR: LENGTHS NOT EQUAL")

    sum = 0
    for i in range(len(officeA)):
        sum += officeA[i][0]
        sum += officeB[i][1]

    if DEBUG:
        print("after balance", officeA, officeB)

    return sum

# print(flight_prices([[40,30],[300,200],[50,50],[30,60]])) # 310
print(flight_prices([[40,30],[300,200],[50,50],[30,60],[100,10], [20,20]])) #340
