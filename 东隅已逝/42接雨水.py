from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        st = []
        res = 0

        for i in range(len(height)):
            while st and height[i] > height[st[-1]]:
                mid = st.pop()
                if not st:
                    break
                left = st[-1]
                width = i - left - 1
                h = min(height[left], height[i]) - height[mid]
                res += width * h
            st.append(i)
        
        return res