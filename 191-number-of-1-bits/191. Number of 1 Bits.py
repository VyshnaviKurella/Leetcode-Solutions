class Solution:
    def hammingWeight(self, n: int) -> int:
        bn = str(bin(n))
        return bn.count("1")


        
        
        
