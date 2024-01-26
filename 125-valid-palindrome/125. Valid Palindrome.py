class Solution:
    def isPalindrome(self, s: str) -> bool:
        # alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        s=s.lower()
        # li = list(s)
        # print(li)
        li =[]
        for i in s:
            if  i.isalnum():
                # print("here")
                # s.replace(i,"")
                # li.remove(i)
                li.append(i)
            
        
        for i in range(int(len(li)/2)):
            if li[i]!=li[len(li)-i-1]:
                return False

        
        return True    