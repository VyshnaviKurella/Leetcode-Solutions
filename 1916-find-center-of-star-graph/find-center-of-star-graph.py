class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        e1 = edges[0][0]
        e2 = edges[0][1]
        if  e1 in edges[1]:
            return e1
        return e2

    