class Solution:
    def romanToInt(self, s: str) -> int:
        strlist = list(s)
        romans = {
            "I": 1,
            "V" :5,
            "X": 10,
            "L":50,
            "C": 100,
            "D":500,
            "M": 1000
        }
        sum=0
        i=0
        while i in range(len(strlist)):
            if strlist[i]== "I":
                if  i+1 < len(strlist) and strlist[i+1]== "V": 
                    sum += 4
                    i=i+1
                elif  i+1 < len(strlist) and strlist[i+1]== "X": 
                    sum += 9
                    i=i+1
                else:
                    sum += 1
                i=i+1
            elif strlist[i]== "X":
                if  i+1 < len(strlist) and strlist[i+1]== "L": 
                    sum += 40
                    i=i+1
                elif   i+1 < len(strlist) and strlist[i+1]== "C": 
                    sum += 90
                    i=i+1
                else:
                    sum += 10
                i=i+1  
            elif strlist[i]== "C":
                if  i+1 < len(strlist) and strlist[i+1]== "D": 
                    sum += 400
                    i=i+1
                elif  i+1 < len(strlist) and strlist[i+1]== "M": 
                    sum += 900
                    print(sum,i)
                    i=i+1
                    print(i)
                else:
                    sum += 100
                i=i+1
            else:
                sum += romans.get(strlist[i])
                i=i+1
                print(sum,i)
                
             

            

        return sum
        