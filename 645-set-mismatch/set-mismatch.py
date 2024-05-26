class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        track = [False] * len(nums)
        res= list()
        for i in nums:
            
          track[i-1] = True if  track[i-1] == False else res.append(i) 

        for i in range(0,len(nums)):
            if track[i] == False:
                res.append(i+1)
        return res