#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

import math

# @lc code=start
class Solution2:
    '''BFS won't work, no matter what branch pruning you do.
    '''
    def get_closest_target(self, cur, targets: set):
        closest_target = -1
        dist = float('inf')
        for target in targets:
            if cur > target:
                if cur - target < dist:
                    dist = cur - target
                    closest_target = target
        return closest_target

    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target:
            return 0
        targets = set([target])
        cur = target
        while cur % 2 == 0:
            cur = cur // 2
            targets.add(cur)
        queue = [startValue]
        visited = set([startValue])
        layer = 0
        ans_lower_bound = float('inf')
        while queue:       # target is always reachable, so the while loop will exit
            layer += 1
            if layer >= ans_lower_bound:
                return ans_lower_bound
            new_queue = []
            for cur in queue:
                if cur < target:
                    nxt = cur * 2           # multiple by 2 iff cur < target
                    if nxt == target:
                        return layer
                    if nxt in targets:      # if in the set targets, then cut branch
                        tmp = int(math.log2(target // nxt + 0.1)) + layer
                        ans_lower_bound = min(tmp, ans_lower_bound)
                    else:
                        if nxt < target:
                            if nxt not in visited:
                                visited.add(nxt)
                                new_queue.append(nxt)
                        else:
                            ans_lower_bound = min(nxt-target+layer, ans_lower_bound)

                nxt = cur - 1               # minus 1 both cur < target and cur > target
                if nxt == target:
                    return layer
                closest_target = self.get_closest_target(nxt, targets)
                if closest_target > 0:
                    tmp = nxt - closest_target + int(math.log2(target // closest_target + 0.1)) + layer
                    ans_lower_bound = min(tmp, ans_lower_bound)
                else:
                    if nxt > 0 and nxt not in visited:
                        visited.add(nxt)
                        new_queue.append(nxt)

            queue = new_queue


class Solution:
    '''think out of the box: switch start and value, then use division and additin.
    '''
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        
        ans += (startValue - target)
        return ans
        

s = Solution()
# print(s.brokenCalc(1, 99999999))
print(s.brokenCalc(1, 1000000000))
# @lc code=end

