"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def Depth(root, depth):
            if root == None:
                return 0
            elif root.children == []:
                return depth + 1
            else:
                maxdepth = 0
                for i in range(len(root.children)):
                    d = Depth(root.children[i], depth + 1)
                    if d > maxdepth:
                        maxdepth = d
                return maxdepth

        return Depth(root, 0)