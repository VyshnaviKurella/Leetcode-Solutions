class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        li=[]
        tsum=0 
        minlen=0
        for i in nums:
            if tsum<target:
                li.append(i)
                tsum=tsum+i
            while tsum>=target:
                if minlen==0:
                    minlen = len(li)
                else:
                    minlen=min(minlen,len(li))
                tsum -= li.pop(0)




        return minlen