# from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if l == k:
            return
            
        if k > l:
            k= k-l

        # temp = nums[l-k:].extend (nums[0:l-k])
        temp = nums[0:l-k]
        temp2 = nums[l-k:]
        temp2.extend(temp)
        for i in range(l):
            nums[i] = temp2[i]

        # print(temp)
      
        """
        Do not return anything, modify nums in-place instead.
        """