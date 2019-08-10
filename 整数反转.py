class Stack(object):
    def __init__(self):
        self._elems=[]
    def empty(self):
        return self._elems==[]
    def push(self,x):
        self._elems.append(x)
    def pop(self):
        if(self.empty()):
            raise ("in SStack.pop()")
        return self._elems.pop()



class Solution(object):
    def reverse(self, x):
        flag=True
        if(x<0):
            x=0-x
            flag=False
        s=str(x)
        q=2147483647
        stack=Stack()
        for i in s:
            stack.push(int(i))
        sum=0
        while( not stack.empty()):
            sum=sum*10+stack.pop()
        if(sum>q):
            return 0
        if(flag):
            return sum
        return 0- sum
