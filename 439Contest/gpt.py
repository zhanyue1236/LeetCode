from typing import List

class Solution:
    def largestAlmostMissingInteger(self, nums: List[int], k: int) -> int:
        count = {}  # 统计所有大小为 k 的子数组中数字的出现次数
        n = len(nums)
        
        # 遍历所有可能的 k 长度的子数组
        for i in range(n - k + 1):
            window = nums[i:i + k]  # 取出当前窗口
            seen = set()  # 防止在同一个窗口内重复计数
            for num in window:
                if num not in seen:
                    count[num] = count.get(num, 0) + 1
                    seen.add(num)

        # 过滤出只出现一次的数（即只在一个子数组中出现过）
        unique_nums = [num for num in count if count[num] == 1]

        # 返回符合条件的最大值，若不存在，返回 -1
        return max(unique_nums) if unique_nums else -1

# 测试
sol = Solution()
print(sol.largestAlmostMissingInteger([0, 0], 2))  # 预期输出：3
