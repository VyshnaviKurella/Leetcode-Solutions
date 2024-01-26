from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = permutations(s1)
        li = set()
        for i in p:
            s = "".join(i)
            li.add(s)
          
        for i in li:
            if i in s2:
                return True