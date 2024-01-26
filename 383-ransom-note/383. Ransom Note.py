class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine= list(magazine)
        count=0
        for i in ransomNote:
            if i in magazine:
                count +=1
                index = magazine.index(i)
                magazine[index]= 1

        if count == len(ransomNote):
            return True
        else:
            return False
