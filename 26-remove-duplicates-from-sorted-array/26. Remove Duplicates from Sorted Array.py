class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
         expectednums= list(set(nums))
         expectednums.sort()
        # tempnums = list(expectednums)
        # tempnums.sort()
         nums[:] = expectednums
         return len(expectednums)
