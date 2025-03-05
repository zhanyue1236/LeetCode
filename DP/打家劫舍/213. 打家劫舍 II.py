from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if n == 0:
            return nums[0]
        nums1 = nums[:-1]
        nums2 = nums[1:]
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]
        dp1[0] = nums1[0]
        dp2[0] = nums2[0]
        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums1[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums2[i])
        return max(dp1[-1], dp2[-1])
        #本质跟打家劫舍1一致，只不过需要分情况讨论
        #return dp[0]