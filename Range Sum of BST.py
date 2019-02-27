# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        # 如果root不存在，則返回0
        if not root:
            return 0

        re = 0
        # 如果root的值大於L小於R的話，root.left 和 root.right都有可能大於L小於R，所以都要加
        if root.val >= L and root.val <= R:
            re += root.val
            re += self.rangeSumBST(root.left, L, R)
            re += self.rangeSumBST(root.right, L, R)
        # 如果root.left 比L還小，那只要搜索right就好，反之亦然
        elif root.val < L:
            re += self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            re += self.rangeSumBST(root.left, L, R)

        return re