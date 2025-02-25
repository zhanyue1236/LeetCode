from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        n = len(s)
        '''
        def isvalid(s, left, right):
            segment = int(s[left: right])
            if not segment:
                return False
            if int(s[left: right]) == 0:
                return True
            elif int(s[left]) == 0:
                return False
            elif int(s[left: right]) <= 255:
                return True
            else:
                return False
                '''
        def isvalid(s, left, right):
            segment = s[left:right]
            if not segment:
                return False
            if segment[0] == '0' and len(segment) > 1:
                return False
            if 0 <= int(segment) <= 255:
                return True
            return False
        def backstracking(s, start_index):
            if len(path) == 3:
                if isvalid(s, start_index, n):
                    path.append(s[start_index: n])
                    result.append(".".join(path))
                    path.pop()
                    return
                else:
                    return
            for i in range(start_index, n):
                if isvalid(s, start_index, i + 1):
                    path.append(s[start_index: i + 1])
                    backstracking(s, i + 1)
                else:
                    #continue
                    break #剪枝，可以直接放弃
                path.pop()
        backstracking(s, 0)
        return result
    
S = Solution()
print(S.restoreIpAddresses("0000"))



                    
                    
