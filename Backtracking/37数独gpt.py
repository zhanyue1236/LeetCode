from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        flag = False

        # 记录行、列、宫格中使用的数字
        row_set = [set() for _ in range(n)]
        col_set = [set() for _ in range(n)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]

        # 初始化填充好的数据
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    num = board[i][j]
                    row_set[i].add(num)
                    col_set[j].add(num)
                    box_set[i//3][j//3].add(num)

        def backtracking(row, col):
            nonlocal flag
            if flag:
                return
            
            if row == n:
                flag = True
                return
            
            if col == n:
                backtracking(row + 1, 0)
                return
            
            if board[row][col] != ".":
                backtracking(row, col + 1)
                return

            for k in range(1, 10):
                k_str = str(k)
                box_r, box_c = row // 3, col // 3
                if k_str not in row_set[row] and k_str not in col_set[col] and k_str not in box_set[box_r][box_c]:
                    # 试探填充
                    board[row][col] = k_str
                    row_set[row].add(k_str)
                    col_set[col].add(k_str)
                    box_set[box_r][box_c].add(k_str)

                    backtracking(row, col + 1)

                    if flag:
                        return

                    # 回溯撤销
                    board[row][col] = "."
                    row_set[row].remove(k_str)
                    col_set[col].remove(k_str)
                    box_set[box_r][box_c].remove(k_str)

        backtracking(0, 0)
