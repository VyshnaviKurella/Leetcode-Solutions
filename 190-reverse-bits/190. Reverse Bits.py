class Solution:
    def reverseBits(self, n: int) -> int:
        li = list(bin(n))
        li= li[2:]
        s=""
        for i in range(1,len(li)+1):
                s =s+ str(li[-i]) 
        for i in range(len(s),32) : 
            s =s+"0"    
        

        return int(s,2)
        