import numpy as np
def convert(s, numRows):
    if(numRows<=1):
        return s
    now=0;
    status=True
    arr={}
    for i in range(numRows+1):
        arr[i]=[]
    Length=len(s)
    global  j
    for j in range(Length):
        if(status):
            if (now <numRows):
                arr[now].append(s[j])
                now += 1
            if(now==numRows):
                now = numRows - 2
                status = False
        else:
            if ( now > 0):
                arr[now].append(s[j])
                #print(s[i], now)
                now = now - 1;
            if(now==0):
                status=True

    p=[]
    for i in range (numRows):
        for j in range(len(arr[i])):
            p.append(arr[i][j])
    return ("".join(p))

