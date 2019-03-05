"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        #即首先把根節點的值放到list中，然後再遍歷其子節點們的值，同時對於每一個子節點也做同樣的操作。
        re = []
        if not root:
            return re
        re.append(root.val)
        for child in root.children:
            re.extend(self.preorder(child))
        return re