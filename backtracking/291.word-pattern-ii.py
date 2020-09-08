"""

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.


Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
 

Constraints:

You may assume both pattern and str contains only lowercase letters.

"""


class Solution:
    '''1. Why use backtracking? Because you don't know which pattern match to which word, so you need to apply a "trial and error" 
          method in a recursion way. And that is backtracking.
       2. What is the route (or path) of the backtracking? I use the index of pattern, i.e. range(0, len(pattern)) 
          as the backtracking route. The index of string, i.e. range(0, len(str)) here is like the directions to search at each pattern index.
       3. Pruning: without prunning, the solution's running time will beat 30+%. After applying prunning, 
          the solution's time will beat 98+%. Here we are pruning the index of strings (the directions to search)
    '''
    def __init__(self):
        self.match = False
        self.pattern = ""
        self.string = ""

    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        if len(pattern) == 0 and len(str) == 0:              # BUG didn't check this edge condition
            return True
        if len(pattern) == 0 or len(str) == 0:
            return False

        self.pattern = pattern
        self.string = str
        d = {}  # pattern --> word
        i, j = 0, 0
        self.backtrack(i, j, d)
        return self.match

    def backtrack(self, i, j, d):
        if self.match:
            return
        if i == len(self.pattern) and j == len(self.string):
            self.match = True
            return
        if i == len(self.pattern) or j == len(self.string):  # BUG: didn't check this
            return

        if self.pattern[i] not in d:
            suffix_len, cur_count = self.prune_helper(i, d)
            for k in range(j+1, len(self.string)+1):         # BUG: no "+1" at len(self.string)+1
                if k + suffix_len + cur_count*(k-j) >= len(self.string) + 1:
                    return                                   # prunning
                word = self.string[j:k]
                if word not in d.values():
                    d[self.pattern[i]] = word
                    self.backtrack(i+1, k, d)
                    d.pop(self.pattern[i])
                if self.match:
                    return
        else:
            word = d[self.pattern[i]]
            if self.string[j:j+len(word)] == word:
                self.backtrack(i+1, j+len(word), d)

    def prune_helper(self, i, d):
        '''the prunning idea here is to reduce the number of unneccessary iterations of k if the following for loop
        '''
        suffix_len, cur_count = 0, 0
        for k in range(i+1, len(self.pattern)):
            if self.pattern[k] in d:
                suffix_len += len(d[self.pattern[k]])
            else:
                if self.pattern[k] == self.pattern[i]:
                    cur_count += 1
                else:
                    suffix_len += 1
        return suffix_len, cur_count

def test():
    pattern = "abab"
    string = "redblueredblue"
    # pattern = "d"
    # string = "ef"
    s = Solution()
    print(s.wordPatternMatch(pattern, string))

test()


'''

"abab"
"redblueredblue"
"aaaa"
"asdasdasdasd"
"aabb"
"xyzabcxzyabc"
""
"s"
"a"
""
""
""
"d"
"e"
"d"
"ef"

'''
