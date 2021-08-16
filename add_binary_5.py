def add_binary(b1,b2):
    longer=""
    shorter=""
    if len(b1)>len(b2): #check length of str not sizes
        longer=b1
        shorter=b2
    else:
        longer=b2
        shorter=b1

    result=""
    carry = 0 
    for i in range(1,len(longer)+1):

        sum=carry + int(longer[-i])
        
        if i<=len(shorter): #must be <= not <
            sum+=int(shorter[-i])

        if sum == 3:
            carry = 1
            result= "1" + result
        elif sum == 2:
            carry =1
            result= "0" + result
        elif sum == 1:
            carry = 0
            result= "1" + result   
        elif sum == 0:
            carry = 0
            result= "0" + result

    
    if carry == 1:
        result= "1" + result 

    return result

print(add_binary("101","100"))