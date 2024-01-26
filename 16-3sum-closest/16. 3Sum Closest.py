
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        i=0
        j= i+1
        k=j+1
        n = len(nums)
        res =  999999

        # while i<n-2 and j<n-1 and k< n:
        while i<n-2:
            while j<n-1:
                 while k<n:
                     sumRes = nums[i]+nums[j]+nums[k] 
                    #  print(sumRes)
                     if sumRes == target:
                         return sumRes
                     if abs(sumRes- target) <= abs(target- res):
                          res = sumRes
                     k= k+1
                 k=j+2
                 j= j+1
            j=i+2
            k=j+1
            i=i+1
        return res
