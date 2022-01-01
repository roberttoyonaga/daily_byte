# use backtracking. There's a DP method too
class Solution(object):
    def __init__(self):
        self.ways = 0
        self.failed = False
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.util(s,0,False)
        if self.failed:
            return 0
        return self.ways
        
    def util(self, s, index, carrying):
        

        if not carrying and s[index] == "0":
            self.failed= True
            return
        if len(s) == index + 1:
            self.ways += 1
            return
        if not carrying :
            if s[index] == "2" and len(s) > index + 1 and s[index+1] <= "6":
                self.util(s, index + 1, True)  
            if s[index] == "1":
                self.util(s, index + 1, True)
                 
        
        if len(s) > index + 1 and s[index+1] != "0":
            self.util(s, index + 1, False)
            