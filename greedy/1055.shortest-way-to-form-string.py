'''

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that 
their concatenation equals target. If the task is impossible, return -1.

'''

from collections import defaultdict, Counter

class Solution:
    '''dp solution is O(n^2 * (n + m)), which will TLE'''
    def shortestWay(self, source: str, target: str) -> int:
        subsequence = {}  # str -> bool
        def is_subsequence(s: str):
            '''check if s is a substring of source
            '''
            if s in subsequence:
                return subsequence[s]
            count = Counter()
            cur = -1
            for ch in s:
                idx_list = sdict[ch]
                while count[ch] < len(idx_list) and idx_list[count[ch]] <= cur:
                    count[ch] += 1
                if count[ch] == len(idx_list):
                    subsequence[s] = False
                    return False
                cur = idx_list[count[ch]]
            subsequence[s] = True
            return True

        # step 1: construct a meta data for source
        sdict = defaultdict(list)
        for i, ch in enumerate(source):
            sdict[ch].append(i)
        # step 2: check if possible or not
        set_source = set(source)
        set_target = set(target)
        for ch in set_target:
            if ch not in set_source:
                return -1
        # step 3: dp
        n = len(target)
        dp = [0] * n
        for i in range(n):
            minn = float('inf')
            if is_subsequence(target[:i+1]):
                dp[i] = 1
                continue
            for j in range(i):
                if dp[j] + 1 >= minn:
                    continue
                if is_subsequence(target[j+1:i+1]):
                    minn = min(minn, dp[j] + 1)
            dp[i] = minn
        return dp[-1]


class Solution:
    '''greedy solution, O(n + m)
    '''
    def shortestWay(self, source: str, target: str) -> int:
        # step 1: construct a meta data for source
        sdict = defaultdict(list)
        for i, ch in enumerate(source):
            sdict[ch].append(i)
        # step 2: check if possible or not
        set_target = set(target)
        for ch in set_target:
            if ch not in sdict:
                return -1
        # step 3: greedy, each time, construct the longest subsequence
        ans = 1
        count = Counter()
        cur = -1
        i = 0
        while i < len(target):
            ch = target[i]
            idx_list = sdict[ch]
            while count[ch] < len(idx_list) and idx_list[count[ch]] <= cur:
                count[ch] += 1
            if count[ch] == len(idx_list):  # "running out" of ch in the sdict
                ans += 1
                count = Counter()
                cur = -1
                continue
            cur = idx_list[count[ch]]
            i += 1
        return ans

# source = "abab"
# target = "abbaba"

source = "jrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvngh"
target = "jrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvnghjrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvnghjrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvnghjrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvnghjrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvnghjrdhoffbzrigocvteqldcrzigccjebjpjjsnldwehfummahsaskzauvpyenrcynxlqwvzzujqryafvngh"

s = Solution()
print(s.shortestWay(source, target))
