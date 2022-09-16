class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        # create a 2D array for result with initial None values
        res=[[None]*rows for k in range(cols)]
        # with every iteration update with transpose values in result array
        for i in range(rows):
            for j in range(cols):
                res[j][i]=matrix[i][j]
        return res
    
    