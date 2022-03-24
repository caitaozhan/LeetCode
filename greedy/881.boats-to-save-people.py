#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    '''greedy: keep trying to put the current heaviest and the lightest on the same boat
    '''
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort(reverse=True)
        heavy = 0
        light = len(people) - 1
        while heavy < light:
            if people[heavy] + people[light] <= limit:
                heavy += 1
                light -= 1
            else:
                heavy += 1
            ans += 1
        if heavy == light:  # in the end, there is only one person
            ans += 1
        return ans

# @lc code=end

