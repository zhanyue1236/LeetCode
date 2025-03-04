from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        m = {}
        n = len(nums)
        for i in range(n - k + 1):
            window = nums[i: i + k]
            seen = set()
            for num in window:
                if num not in seen:
                    m[num] = m.get(num, 0) + 1
                    seen.add(num)

        unique_nums = [num for num in m if m[num] == 1]
        return max(unique_nums) if unique_nums else -1

S = Solution()
print(S.largestInteger([0, 0], 2))

