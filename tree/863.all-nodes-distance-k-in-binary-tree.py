#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    
    def __init__(self):
        self.path_to_target = None  # BUG: having a member here makes things easier
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs_to_target(root, target, stack, found):
            if root is None:
                return
            if root is target:
                found[0] = True
                stack.append(root)
                self.path_to_target = stack[:]  # BUG: made a mistake by using deepcopy...
            if found[0]:
                return
            
            stack.append(root)
            dfs_to_target(root.left, target, stack, found)
            dfs_to_target(root.right, target, stack, found)
            stack.pop()


        def get_nodes(root, distance, nodes):
            if root is None:
                return
            if distance == 0:
                nodes.append(root)
                return
            
            get_nodes(root.left, distance - 1, nodes)
            get_nodes(root.right, distance - 1, nodes)

            
        stack = []
        found = [False]
        dfs_to_target(root, target, stack, found)
        # for node in self.path_to_target:
        #     print(node.val)

        nodes = []
        length = len(self.path_to_target)
        for i in range(length):
            if self.path_to_target[i] is not target:  # is not target, need to avoid searching one side that contains the target
                distance_to_target = length - 1 - i
                distance = k - distance_to_target
                if distance < 0:
                    pass
                elif distance == 0:
                    nodes.append(self.path_to_target[i])
                else:
                    subroot = None
                    if self.path_to_target[i].left is self.path_to_target[i + 1]:
                        subroot = self.path_to_target[i].right
                    else:
                        subroot = self.path_to_target[i].left
                    distance -= 1
                    get_nodes(subroot, distance, nodes)
            else:                                  # is target, then simple, just search under the target
                get_nodes(self.path_to_target[i], k, nodes)

        ans = []
        for node in nodes:
            ans.append(node.val)
        return ans


# @lc code=end

