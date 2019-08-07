import numpy as np
maxlen=0
S=""
def suan(s):
    p=len(s)
    q=int(p/2)
    for i in range(q):
        if(s[i]==s[p-i-1]):
            continue
        else:
            return False
    global  maxlen
    global S
    if(len(s)>maxlen):
       maxlen=len(s)
       S=s
class Solution(object):
    def longestPalindrome(self, s):
        if(len(s)==1):
            return s
        global maxlen,S
        S=""
        maxlen=0
        Length=len(s)
        for i in range (Length):
            for j in range(i,Length+1):
                suan(s[i:j])
        return S