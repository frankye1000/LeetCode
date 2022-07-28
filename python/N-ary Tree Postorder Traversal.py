# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def postorder(self, root):
        re = []
        if not root:
            return re

        for child in root.children:
            re.extend(self.postorder(child))

        re.append(root.val)

        return re
