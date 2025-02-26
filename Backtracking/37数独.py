from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        flag = 0
        def isvalid(board, row, col, k_str):
            for i in range(n):
                if k_str == board[i][col]:
                    return False
            for j in range(n):
                if k_str == board[row][j]:
                    return False
            #r = int(row / 3)
            #s = int(col / 3)
            r, s = row // 3, col // 3#别用这个int强转了
            for k in range(r * 3, r * 3 + 3):
                for q in range(s * 3, s * 3 + 3):
                    if k_str == board[k][q]:
                        return False
            return True
        def backtracking(row, col):
            nonlocal flag
            if flag == 1:
                return
            
            #第一步先检查row, 找到了直接跳过
            if row == 9:
                flag = 1
                return
                
            #先检查col, 防止index out of range
            if col == 9:
                backtracking(row + 1, 0)
                return
            
            #提速，如果已经被占住了，直接下一步
            if board[row][col] != ".":
                backtracking(row, col + 1)
                return
            
        
            for k in range(1, 10):
                k_str = str(k)
                if isvalid(board, row, col, k_str):
                    board[row][col] = k_str
                    backtracking(row, col + 1)
                    if flag == 1:
                        return
                    #backtracking(row + 1, 0) #col进入下一行是0，并且可以不用在这里搞，放到col == 0 那边
                    #backtracking(row + 1, col)
                    board[row][col] = "."
        backtracking(0, 0)
