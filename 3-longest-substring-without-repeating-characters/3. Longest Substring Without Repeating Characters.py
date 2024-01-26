class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub =[]
        reslen=0
        for i in s:
            if i not in sub:
                sub.append(i)
            else:
                reslen= max(reslen,len(sub))
                # sub.clear()
                n=sub.index(i)
                sub = sub[n+1:]
                sub.append(i)
        reslen = max(reslen,len(sub))
            # return len(sub)
        # if len(s)>0 and reslen==0:
        #     reslen= len(s)
        return reslen