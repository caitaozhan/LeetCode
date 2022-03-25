#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
class Solution:
    '''greedy: deal with the larger abs(costa-costb) first.
    '''
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
        ans = 0
        a, b = 0, 0
        n = len(costs) // 2
        for costa, costb in costs:
            if a == n:        # A is full, go to B
                ans += costb
                continue
            if b == n:        # B is full, go to A
                ans += costa
                continue

            if costa < costb:
                ans += costa
                a += 1
            else:
                ans += costb
                b += 1
        
        return ans
                
        


# @lc code=end

