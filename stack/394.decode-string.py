#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (49.17%)
# Likes:    3570
# Dislikes: 177
# Total Accepted:    230.7K
# Total Submissions: 457.7K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# 
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        expand = []
        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(i)
            if ch == ']':
                left = stack.pop()
                expand.append((left, i))

        s_list = list(s)
        # self.print(s_list)

        for l, r in expand:
            sub = s_list[l+1:r]
            repeat, length = self.get_repeat(s_list, l)
            sub = repeat * ''.join(sub)
            s_list[l-length] = sub
            for i in range(l-length+1, r+1):
                s_list[i] = ''              # maintain the index by inserting ''
            # self.print(s_list)
        return ''.join(s_list)

    def get_repeat(self, s_list, r):
        l = r - 1
        while s_list[l].isdigit():
            l -= 1
        l += 1
        return int(''.join(s_list[l:r])), r-l

    def print(self, listt):
        for e in listt:
            if e == '':
                print('-', end='')
            else:
                print(e, end=' ')
        print()


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                string_list = []
                while stack[-1] != '[':
                    string_list.append(stack.pop())
                stack.pop()
                string = ''.join(reversed(string_list))
                num_list = []
                while stack and stack[-1].isdigit():
                    num_list.append(stack.pop())
                num = ''.join(reversed(num_list))
                new_string = string * int(num)
                stack.append(new_string)
        return ''.join(stack)




# @lc code=end

"""

"100[leetcode]"
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
"abc3[cd]xyz"

"""