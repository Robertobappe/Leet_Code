class Solution:
    def isPalindrome(self,x:int) -> bool:
        self.x = str(x)
        a,b = '',''
        for i in self.x:
           a+= i
        for j in range(len(self.x)-1,-1,-1):
            b+=self.x[j]

        if a == b:
            return True
        else:
            return False
        