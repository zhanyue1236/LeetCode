from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isvalid(chessboard, row, coloumn):
            #只检查列
            for j in range(row):
                if chessboard[j][coloumn] == "Q":
                    return False
            i, j = row - 1, coloumn - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, coloumn + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
        result = []
        chessboard = [["." for i in range(n)] for i in range (n)]
        def backtracking(start_index):
            if start_index == n:
                result.append(["".join(item) for item in chessboard])
                return
            for i in range(n):
                if isvalid(chessboard,start_index, i):
                    chessboard[start_index][i] = "Q"
                    backtracking(start_index + 1)
                    chessboard[start_index][i] = "."
        backtracking(0)
        return result
#问题：isvalid的判断问题？有两个方法：1.（我的）先放置，然后判断当前棋盘是否合法。但是这样显然很慢，所以应该用第二个方法：
# 2.先判断当前位置会不会被攻击，如果不会被攻击，那么就好，因为这里的棋盘本来就是合法的，其他位置其实并不需要检查。（做多活了）
#2.5同时再做精简，因为此时我们做到第row行，(1) row后面的都不会出现，所以左下右下都不需要看；(2)只需要看列，因为行是一个个来的，不会有重复，并且只需要看上面的列。

s = Solution()
print(s.solveNQueens(4))
'''
n = 3
c = []
chessboard = [['.' for i in range(n)] for i in range (n)]
for item in chessboard:
    temp = ''.join(item)
    c.append(temp)

print(c)'''