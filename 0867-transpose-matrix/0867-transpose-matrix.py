class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        
        res = []
        for i in range(m):
            res.append([0] * n)
        
        for i in range(n):
            for j in range(m):
                res[j][i] = matrix[i][j]
        
        return res
