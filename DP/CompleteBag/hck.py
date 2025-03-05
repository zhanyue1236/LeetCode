from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tmp = s
        done = False
        while not done:
            flag1
            for word in wordDict:
                if tmp.startswith(word):
                    tmp = tmp[len(word):]
                    goto flag1
                else:
                    break

            
            if len(tmp) == 0:
                return True
            else:
                return False