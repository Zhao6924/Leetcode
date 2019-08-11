class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag = True
        sum = 0
        Len = len(str)
        for i in range(Len):
            if (str[i] == " "):
                continue
            if (str[i] == "-"):
                flag = False
                continue
            if( not str[i].isdigit()):
                continue
            sum = sum * 10 + int(str[i])
        if (sum > 2147483647):
            if (not flag):
                #print(-2147483647)
                return -2147483647
            else:
                return 2147483647
        else:
            if (flag):
                return sum
            else:
                return 0 - sum
q=Solution()
