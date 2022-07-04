#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

from typing import List

# @lc code=start
class Solution:
    '''O(nlogn) solution using sorting
    '''
    def candy(self, ratings: List[int]) -> int:
        def ratings_help(i):
            if i == -1:
                return 10**5
            if i >= len(ratings):
                return 10**5
            return ratings[i]

        ratings_sorted = sorted([(rating, i) for i, rating in enumerate(ratings)])
        candy = [0] * len(ratings)
        for rate, i in ratings_sorted:
            left = i - 1
            right = i + 1
            left_ratings = ratings_help(left)
            right_ratings = ratings_help(right)
            if rate <= left_ratings and rate <= right_ratings:
                candy[i] = 1
            elif rate > left_ratings and rate <= right_ratings:
                candy[i] = candy[left] + 1
            elif rate <= left_ratings and rate > right_ratings:
                candy[i] = candy[right] + 1
            else:
                candy[i] = max(candy[left], candy[right]) + 1
                
        return sum(candy)


class Solution:
    '''O(n) solution doing a left to right pass and right to left pass
    '''
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for  i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1]+1)
        return sum(candy)




# @lc code=end

