# [1660] Correct a binary tree


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        val2parent = {} # node.val --> parent node
        queue = [root]
        while queue:
            new_queue_set = set()
            new_queue = []
            for node in queue:
                # check if node in the next layer
                if node.val in new_queue_set:
                    invalid = val2parent[node.val]
                    invalid_parent = val2parent[invalid.val]
                    if invalid_parent.left == invalid:
                        invalid_parent.left = None
                    else:
                        invalid_parent.right = None
                    return root

                if node.left:
                    val2parent[node.left.val] = node
                    new_queue.append(node.left)
                    new_queue_set.add(node.left.val)
                if node.right:
                    val2parent[node.right.val] = node
                    new_queue.append(node.right)
                    new_queue_set.add(node.right.val)
                    
            queue = new_queue