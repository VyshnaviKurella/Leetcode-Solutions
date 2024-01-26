class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        t = s.split(" ")
        t.reverse()
        res=""
        print (t)
        for i in t:
            if i!= "":
                if res =="":
                    res = res+i
                else:
                    res = res + " "+ i
        # res = res.strip()
                
        return res