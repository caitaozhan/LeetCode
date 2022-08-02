#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

from tpying import List
from collections import Counter

# @lc code=start
class Solution:
    '''O(m*n)
    '''
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def is_subset(c1: Counter, c2: Counter) -> bool:
            '''
            return True if c2 is a subset of c1, else False
            '''
            for key, val in c2.items():
                if key not in c1 or c1[key] < val:
                    return False
            return True

        counter1 = []
        counter2 = []
        for word in words1:
            counter1.append(Counter(word))
        words2 = set([''.join(sorted(word)) for word in words2])
        for word in words2:
            counter2.append(Counter(word))
        
        ans = []
        for i, c1 in enumerate(counter1):
            for c2 in counter2:
                if not is_subset(c1, c2):
                    break
            else:
                ans.append(words1[i])
        return ans


class Solution:
    '''O(m + n)
       the time reduction is done by the following observation: all the counter of words in words2 can be "combined"
    '''
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def is_subset(c1: Counter, c2: Counter) -> bool:
            '''
            return True if c2 is a subset of c1, else False
            '''
            for key, val in c2.items():
                if key not in c1 or c1[key] < val:
                    return False
            return True

        counter = Counter()   # a superset of counters of all words in words2
        for word in words2:
            c = Counter(word)
            for key, val in c.items():
                if val > counter[key]:
                    counter[key] = val
        ans = []
        for word in words1:
            c = Counter(word)
            if is_subset(c, counter):
                ans.append(word)
        return ans


# @lc code=end

