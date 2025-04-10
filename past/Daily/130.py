class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        par = int(len(s) / (k * 2))
        res = ""
        for i in range(par):
            mnum = i * 2 * k
            mid1 = s[mnum: mnum + k][::-1] #切片反转,同样可以使用切片步长
            mid2 = s[mnum + k:mnum + k + k]
            res += mid1
            res += mid2
        remain = k - (par * 2 * k)
        if remain <= k:
            res += s[remain::][::-1]
        else:
            res += s[remain:remain + k:][::-1]
            res += s[remain+k::]
        return res
