class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        char_list = list()
        res = list()
        for i in range(0,len(s)) :
            if s[i] == c:
                char_list.append(i)
        for i in range(0,len(s)): 
                # closest = min(char_list,key = lambda x: abs(x-i)) // returns the min value of char_list instead of abs(x-i)value
                closest = min(abs(x-i) for x in char_list)
                res.append(closest)
            

        return res
