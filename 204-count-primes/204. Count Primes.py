class Solution:
    def countPrimes(self, n: int) -> int:
        if n== 0 or n ==1:
            return 0
        primes =0
        for i in range(2,n):
            c =0
            for j in range(1,i+1):
                # print(i,j)
                if i%j == 0:
                    c +=1
            if c==2:
                primes +=1
        return primes
            
                


        
