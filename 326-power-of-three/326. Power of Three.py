class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
             return False
        for i in range(20):
            if n == pow(3,i):
                return True
        return False
       
       
        # if n ==0:
        #     return False
        # res = pow(n,1/3)
        # if(type(res) == float ):
        #     res= (res*10)%10
        # else:
        #     return False
        # if res == 0.0:
        #     return True
        # return False
        
