class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if n== pow(2,i):
                return True
        return False