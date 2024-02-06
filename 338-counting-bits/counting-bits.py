class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = list()

        for i in range(n+1):
            count =0
            while(i!=0):
                i = i& (i-1)
                count +=1
            ans.append(count)
        
        return ans


        