class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len1 = 0 
        len2 = len(height)-1 
        max_water = 0  

        while len1<len2 :
            if height[len1] >= height[len2]:
                max_water = max(max_water,(len2-len1) *height[len2])
                len2 -=1
            
            else:
                max_water = max(max_water,(len2-len1)*height[len1] )
                len1 +=1
        return max_water
            

        