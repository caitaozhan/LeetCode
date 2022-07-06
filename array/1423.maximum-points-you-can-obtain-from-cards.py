#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

from typing import List

# @lc code=start
class Solution:
    '''O(n) time and O(n) space
    '''
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        prefixsum = [0] * n
        prefixsum[0] = cardPoints[0]
        for i in range(1, n):
            prefixsum[i] = prefixsum[i-1] + cardPoints[i]
        suffixsum = [0] * n
        suffixsum[n-1] = cardPoints[n-1]
        for i in range(n-2, -1, -1):
            suffixsum[i] = suffixsum[i+1] + cardPoints[i]
        
        ans = max(suffixsum[n-k], prefixsum[k-1])
        i = 0
        while i < k-1:
            j = n - k + i + 1
            ans = max(ans, prefixsum[i] + suffixsum[j])
            i += 1

        return ans


class Solution:
    '''O(k) time and O(k) space
    '''
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)

        prefixsum = [0] * k
        prefixsum[0] = cardPoints[0]
        for i in range(1, k):
            prefixsum[i] = prefixsum[i-1] + cardPoints[i]
        prefixsum.insert(0, 0)

        suffixsum = [0] * k
        suffixsum[k-1] = cardPoints[n-1]
        for i in range(1, k):
            suffix_i = k - 1 - i
            card_i   = n - 1 - i 
            suffixsum[suffix_i] = suffixsum[suffix_i + 1] + cardPoints[card_i]
        suffixsum.append(0)

        ans = 0
        i = 0
        while i < k+1:
            ans = max(ans, prefixsum[i] + suffixsum[i])
            i += 1

        return ans



class Solution:
    '''O(k) time and O(1) space
       no prefixsum or suffixsum, use two pointers
    '''
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        j = n - k
        sum_j = sum(cardPoints[j:])
        ans = sum_j

        i = 0
        sum_i = 0
        while i < k:
            sum_i += cardPoints[i]
            sum_j -= cardPoints[j]
            ans = max(ans, sum_i + sum_j)
            i += 1
            j += 1
        
        return ans





cardPoints = [1,2,3,4,5,6,1]
k = 3
cardPoints = [2,6,4,3,1,7]
k = 4
s = Solution()
print(s.maxScore(cardPoints, k))

# @lc code=end

