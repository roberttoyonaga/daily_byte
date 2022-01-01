#this function is allowed to make 1 deletion 

def valid_palindrome(str):

    start = 0 
    end = len(str) - 1

    deletion_count = 0 

    while start < end:

        #handle unequal cases
        if str[start] != str[end]:
            if deletion_count > 0:
                return False
            
            deletion_count += 1

            #explore both cases
            if str[start+1] == str[end]:
                start += 1
            elif str[start] == str[end-1]:
                end -= 1
            else:
                return False

        start+=1
        end-=1

    return True

print(valid_palindrome('foobof'))
print(valid_palindrome('abccab'))




