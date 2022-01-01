'''Given a string of digits, return all possible text messages those digits could send. '''

class Solution:
    def __init__(self):
        self.digit_to_chars = {'0':None, '1':None, '2':['a','b','c'],'3':['d','e','f'], '4':['g','h','i'],'5':['j','k','l'], '6':['m','n','o'], '7':['q','p','r','s'],'8':['t','u','v'], '9':['w','x','y','z']}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) is 0:
            return []
        ret = []
        self.util(ret, "", digits, 0)
        return ret

    def util(self, ret, current,digits,index):
        if index == len(digits):
            ret.append(current)
            return
        available_chars = self.digit_to_chars[digits[index]]
        for char in available_chars:
            self.util(ret, current+char, digits,index+1)
            
digit_to_chars = {'0':None, '1':None, '2':['a','b','c'],'3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['q','p','r','s'],'8':['t','u','v'], '9':['w','x','y','z']}

def generate_text_messages(nums, s, index, result):
    if index == len(nums):
        result.append(s) # only append when we reach out stopping condition (at the leaves)
        return

    # recurse for each possible next letter
    available_letters = digit_to_chars[nums[index]]

    # the number maps to nothing, ignore
    if available_letters is None:
         generate_text_messages(nums, s, index + 1, result)
    else:
        for letter in available_letters:
            generate_text_messages(nums, s + letter, index + 1, result)


r= []
generate_text_messages("02013","",0,r)
print(r)
    


            

