# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        m = 0
        q = [root]

        while len(q) != 0:
            m += 1

            new_q = []
            for node in q:
                if not node.left and not node.right:
                    return m
                if node.right:
                    new_q.append(node.right)
                if node.left:
                    new_q.append(node.left)
            q = new_q
        return m