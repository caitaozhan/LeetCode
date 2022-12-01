#
# @lc app=leetcode id=936 lang=python3
#
# [936] Stamping The Sequence
#

from typing import List

# @lc code=start
class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def find_all(s: str, sub: str):
            indx = []
            start = 0
            while True:
                start = s.find(sub, start)
                if start == -1:
                    break
                indx.append(start)
                start += len(sub)
            return indx

        def update_target(target, indx, n):
            target = list(target)
            for i in indx:
                for j in range(n):
                    target[i+j] = '?'
            return ''.join(target)

        ans = []
        n = len(stamp)
        indx = find_all(target, stamp)
        found = False
        if indx:
            found = True
            ans.extend(indx)
            target = update_target(target, indx, n)
        
        while found is True:
            found = False
            for i in range(n - 1, 0, -1):
                length = (n - i)
                question = '?' * length
                stamp_left = stamp[:(n-length)] + question   # abc??
                stamp_right = question + stamp[length:]      # ??cde
                indx = find_all(target, stamp_left)
                while indx:
                    found = True
                    ans.extend(indx)
                    target = update_target(target, indx, n)
                    indx = find_all(target, stamp_left)
                indx = find_all(target, stamp_right)
                while indx:
                    found = True
                    ans.extend(indx)
                    target = update_target(target, indx, n)
                    indx = find_all(target, stamp_right)
            if target == '?' * len(target):
                return ans[::-1]
        return []

stamp = "abca"
target = "aabcaca"

stamp = "oz"
target = "ooozz"

stamp = "abc"
target = "ababc"

stamp = "uskh"
target = "uskhkhhskh"

stamp = "v"
target = "v"

stamp = "zbs"
target = "zbzbsbszbssbzbszbsss"

s = Solution()
print(s.movesToStamp(stamp, target))
        
# @lc code=end

