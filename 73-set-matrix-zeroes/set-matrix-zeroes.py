class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows =list()
        cols = list()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] ==0:
                    print(row,col)
                    if row not in rows:
                        rows.append(row)
                    if col not in cols:
                        cols.append(col)
        
        for i in rows:
            matrix[i]= [0]*len(matrix[0])
        
        for i in cols:
            for row in range(len(matrix)):
                matrix[row][i] = 0
        print(rows,cols)

        
        






        