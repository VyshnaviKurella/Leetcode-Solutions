class Solution:
    def decodeString(self, s: str) -> str:
    
        # global res
        res = ""
        i = 0
        def rec(t:int) :
            re = ""
            num = s[t]
            while s[t+1] != "[":
                    num = num+s[t+1]
                    t=t+1
            num = int(num)
            # print(num)
            t=t+2
            temp =""
            while t <len(s) and s[t]!="]": 
                if s[t].isalpha():
                    re= re + s[t]

                if s[t].isdigit():
                    r = rec(t)
                    re =re + r[0]
                    t = r[1]
                t +=1
            temp = temp+re   
            while num>1:
                re = re +temp 
                num -=1
            return [re,t]

        
        while i < len(s):
            if s[i].isdigit():
                r = rec(i)
                res = res+  r[0]
                i = r[1]

            elif s[i].isalpha():
                res = res+ s[i]
                # print(res)
            else:
                continue
            i +=1
        
        return res

