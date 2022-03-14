#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # step 1: deal with /
        path += '/'          # BUG for test case: "/a//b////c/d//././/.."
        directory = []
        last_slash = 0
        for i in range(1, len(path)):
            if path[i] == '/':
                if path[i-1] != '/':
                    directory.append(path[last_slash+1:i])
                last_slash = i

        # step 2: deal with directory
        stack = []
        for d in directory:
            if d == '.':
                pass
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)

class Solution:
    '''a better step 1 dealing with / '''
    def simplifyPath(self, path: str) -> str:
        # step 1
        directory = [s for s in path.split('/') if s]

        # step 2
        stack = []
        for d in directory:
            if d == '.':
                pass
            elif d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return '/' + '/'.join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        return os.path.realpath(path)
# @lc code=end

