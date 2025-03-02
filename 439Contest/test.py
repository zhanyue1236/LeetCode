class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            ss = ""
            for i in range(len(s) - 1):
                a = int(s[i])
                b = int(s[i + 1])
                c = str((a + b) % 10)
                ss += c
            s = ss
        return s[0] == s[1]
    
S = Solution()
print(S.hasSameDigits("3902"))
