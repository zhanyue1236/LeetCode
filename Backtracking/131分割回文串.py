from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        n = len(s)
        def isBack(lst, left, right):
            n = len(lst)
            while left <= right:
                if lst[left] == lst[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        def backtracking(s, start_index):
            if start_index >= n:
                result.append(path.copy())
                return
            for i in range(start_index, n):
                if isBack(s, start_index, i):
                #if s[start_index: i + 1] == s[start_index: i + 1][::-1]:#注意逆序！！！
                    path.append(s[start_index: i + 1])
                    backtracking(s, i + 1)
                else:
                    continue
                #backtracking(s, i + 1)
                path.pop()
        backtracking(s, 0)
        return result
    
S = Solution()
print(S.partition("aab"))