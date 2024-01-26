class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # m*n == r*c then  matrix possible
        li=[]
        m=0
        k=0
        if(len(mat)* len(mat[0]) == r*c):           
            for i in range(r):
                temp =[]            
                # for j in range(int (c/len(mat[0]))):
                #     temp.extend(mat[j]) 
                # # prnt(m,k)
                # print(c/len(mat[0]))

                # if c /len(mat[0]) <1 :
                for j in range(c):
                        temp.append(mat[m][k])
                        k=k+1
                        if( k  == len(mat[0])):
                            m =m+1
                            k=0

                li.append(temp)
            return li
        return mat
                    


                    


   
          
