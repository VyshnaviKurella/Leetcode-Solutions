
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getlength(str):
            return len(str)
        strs.sort( key = getlength)
        res=""
        for i in range(len(strs[0])+1):
            
            lenp=0
            for j in range(len(strs)):
                if strs[0][:i] in strs[j][:i]:
                     lenp +=1
        
            if lenp == len(strs):
                 res = strs[0][:i]

        return res