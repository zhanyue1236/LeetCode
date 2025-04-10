from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = [] #一些同学可能想了：我把所有组合求出来，再用set或者map去重，这么做很容易超时！, 加used
        used = []
        candidates = sorted(candidates)
        #print(candidates)
        def backtracking(candidates, start_index):
            if sum(path) == target:
                result.append(path.copy())
                return
            elif sum(path) > target:
                return
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]: #i > start_index这里就指的是说明你现在不是递归下去了，而且同层！
                    continue
                path.append(candidates[i])
                backtracking(candidates, i + 1)
                path.pop()
        backtracking(candidates, 0)
        return result
S = Solution()
print(S.combinationSum2([10,1,2,7,6,1,5], 8))
