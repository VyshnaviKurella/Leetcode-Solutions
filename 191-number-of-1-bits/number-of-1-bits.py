class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n= list(bin(n))
        count=0
        # print(n)
        for i in range(len(n)):
            if n[i] == "1":
                count +=1
        return count


