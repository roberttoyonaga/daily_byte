
counter = 0    
def message_decryption(nums):
    global counter
    counter =1
    util(nums)
    return counter
    
def util(nums):
    if len(nums) ==0:
        return
    global counter
    if len(nums)>1 and (nums[0] =="1" or nums[0] =="2") and int(nums[1]) < 6:
        counter +=1
        util(nums[2:])
    util(nums[1:])

   
print(message_decryption("1234"),3)
print(message_decryption("23"),2)
print(message_decryption("22313"),6)
'''
2 2 3 1 3 
22 3 1 3
22 3 13
2 2 3 13
2 23 1 3
2 23 13
'''

