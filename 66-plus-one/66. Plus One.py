class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strval=""
        for i in digits:
            strval = strval + str(i)
        strval = int(strval)+1
        val=[]
        for i in str(strval):
            val.append(int(i))
        
        return val
       # return []
        
