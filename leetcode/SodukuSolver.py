board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.':
                    for val in range(1,9):
                        if issafe(r,c,board,val):
                            board[r][c] = val
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[r][c] = '.'
                return False             
        return True
    def issafe(self,r,c,board,val):
        for i in range(cols):
            if board[r][i] == val:
                return False
            if board[i][c] == val:
                return False
            if board[3*(r/3)+i/3][3*(c/3)+i%3] == val:
                return False
        return True