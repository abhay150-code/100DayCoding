class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(i, j, val):
            for k in range(9):
                if k != j and board[i][k] == val:
                    return False

            for k in range(9):
                if k != i and board[k][j] == val:
                    return False

            start_row = (i // 3) * 3
            start_col = (j // 3) * 3

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if (r != i or c != j) and board[r][c] == val:
                        return False

            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not isValid(i, j, board[i][j]):
                        return False

        return True