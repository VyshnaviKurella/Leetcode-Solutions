class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        s= s.strip()
        words =  s.split(" ")
        return len(words[-1])
        '''
        count=0
        slen = len(s)
        for i in range(slen):
            if s[slen-i -1]==" " and count == 0:
                continue
            elif s[slen-i-1] == " " and count >0:
                break
            elif s[slen-i-1] != " ":
                 count +=1
                 print(count,s[slen-i-1])
        return count


