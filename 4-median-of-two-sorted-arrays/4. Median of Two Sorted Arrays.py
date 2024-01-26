class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        print(n/2)
        if n%2!=0:
            return float(nums1[int(n/2)])
            
        else:
            return float ((nums1[int(n/2)]+ nums1[int(n/2)-1])/2)
    