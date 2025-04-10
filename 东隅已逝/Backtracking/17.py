from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        path = []
        result = []
        digit_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        def backtracking(digits, index):
            if len(path) == n :
                paths = path.copy()
                result.append("".join(paths))
                return
            for i in range(index, n):
                temp_letter = digit_map[int(digits[index])]
                for item in temp_letter: #回溯里能用for做的就用for做，用不了for做的再用递归（无法控制n）
                    path.append(item)
                    backtracking(digits, i + 1)
                    path.pop()
        backtracking(digits, 0)
        return result

S = Solution()
print(S.letterCombinations("5"))
                    

                
    