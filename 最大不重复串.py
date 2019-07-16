class Solution:
     def lengthOfLongestSubstring(self, s):
         if(len(s)==0):
             return 0;
         length=len(s)
         lookup=set()
         maxlen=0;
         nowlen=0;
         index=0
         for i in range(0,length):
             nowlen+=1
             while(s[i] in lookup):
                 lookup.remove(s[index])
                 index+=1;
                 nowlen=nowlen-1
             lookup.add(s[i])
             maxlen=max(maxlen,nowlen)
         return maxlen