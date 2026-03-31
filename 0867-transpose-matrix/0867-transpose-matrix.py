class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        
        res = []
        for i in range(m):
            res.append([0] * n)
        
        def solve(i, j):
            if i == n:
                return
            if j == m:
                solve(i + 1, 0)
                return
            
            res[j][i] = matrix[i][j]
            solve(i, j + 1)
        
        solve(0, 0)
        return res