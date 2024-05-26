class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum =0
        for i in range(0,len( nums)):
            if bin(i).count('1') == k:
                sum +=nums[i]
        return sum
