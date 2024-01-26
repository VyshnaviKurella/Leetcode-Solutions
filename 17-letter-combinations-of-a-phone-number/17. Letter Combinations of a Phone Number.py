class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)) == 0:
            return []
        di = {"2": "abc","3": "def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if(len(digits))==1:
            return list(di.get(digits))
        res =[]
        for i in range(len(digits)):
            n = list(di.get(digits[i]))
            if len(res) ==0:
                for i in n:
                    res.append(i)
            else:
                temp =[]
                for i in res:
                    for j in n:
                        temp.append(i+j)
                res = temp.copy()
                # print(res)
             
        
        return res