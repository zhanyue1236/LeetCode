from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        sorted(nums)
        n = len(nums)
        m = n // 2
        s = sum(nums)
        path = []
        res = 999999999
        def backtracking(start_index):
            nonlocal res
            if len(path) == m:
                res = min(res, abs(s - 2 * sum(path)))
                return
            for i in range(start_index, n):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
        backtracking(0)
        return res
    
S = Solution()
print(S.minimumDifference([3,9,7,3]))
#超时（包超时的牢底）