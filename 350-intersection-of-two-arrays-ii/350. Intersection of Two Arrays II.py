class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        if len(nums1)> len(nums2):
            for i in nums2:
                if i in nums1:
                    ind = nums1.index(i)
                    nums1[ind]= -1
                    li.append(i)
        else:
             for i in nums1:
                if i in nums2:
                    ind = nums2.index(i)
                    nums2[ind]= -1
                    li.append(i)


        return li