class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l =len(columnTitle)
        di = {
            "A" :1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26

        }
        num=0
        for i in range(l): 
            t=di.get(columnTitle[i])           
            num += 26**(l-i-1)  *t 
            print(num)
            # print(di.get(columnTitle[i]))
            # if(i==l-1):
                
                # num = num+ t
            
        # print(num)    
            # only for the last digit get value
        return num