#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (59.60%)
# Likes:    1721
# Dislikes: 33
# Total Accepted:    58.8K
# Total Submissions: 95.6K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# In a country popular for train travel, you have planned some train travelling
# one year in advance.  The days of the year that you will travel is given as
# an array days.  Each day is an integer from 1 to 365.
# 
# Train tickets are sold in 3 different ways:
# 
# 
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# 
# 
# The passes allow that many days of consecutive travel.  For example, if we
# get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6,
# 7, and 8.
# 
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
# 
# 
# 
# Example 1:
# 
# 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# 
# 
# 
# Example 2:
# 
# 
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#

# @lc code=start

from typing import List

class Node:
    def __init__(self, valid_to, cost):
        self.valid_to = valid_to
        self.cost = cost
    
    def __str__(self):
        return f'valid to {self.valid_to}, cost is {self.cost}'

class Solution:
    '''it is like doing a bfs in a tree. you are actually creating the tree.
    '''
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        root = Node(0, 0)
        # active_nodes = [root]
        active_nodes = {0:root}
        ans = float('inf')
        valid = [1, 7, 30]
        for day in days:
            print(day)
            new_active_nodes = {}
            for node in active_nodes.values():
                if day <= node.valid_to:  # not buying a new ticket
                    if new_active_nodes.get(node.valid_to) is None:
                        new_active_nodes[node.valid_to] = node
                    if new_active_nodes.get(node.valid_to) is not None and new_active_nodes[node.valid_to].cost > node.cost:
                        new_active_nodes[node.valid_to] = node
                else:                     # buying a new ticket
                    for i, cost in enumerate(costs):
                        new_node = Node(day + valid[i] - 1, node.cost + cost)
                        print(new_node)
                        if new_node.valid_to >= days[-1]:
                            ans = min(ans, new_node.cost)
                        else:
                            if new_active_nodes.get(new_node.valid_to) is None:
                                new_active_nodes[new_node.valid_to] = new_node
                            else:
                                if new_active_nodes[new_node.valid_to].cost > new_node.cost:
                                    new_active_nodes[new_node.valid_to] = new_node
            active_nodes = new_active_nodes
            length = len(active_nodes)
            print(f'len = {length}')
        return ans

def test():
    days = [1,5,7,10]
    costs = [2,7,15]

    # days = [1,4,6,7,8,20]
    # costs = [2,7,15]
    s = Solution()
    print(s.mincostTickets(days, costs))


test()

# @lc code=end

