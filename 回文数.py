class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        q=str(x)
        Len=len(q)
        for i in range(Len):
            if(q[i]==q[Len-1-i]):
                continue
            else:
                return False
        return True