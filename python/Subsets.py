class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums1 = [[i] for i in nums]
        returnn=[[i] for i in nums]
        for n in returnn:
            for u in nums1:
                ap = sorted(list(set(n+u)))
                if ap not in returnn:
                    returnn.append(ap)
        returnn.append([])
        return returnn




######################################################################
## 用combinations套件
# from itertools import combinations
#
# l=[]
# for i in range(len(nums)+1):
#     com = combinations(nums,i)
#     l.extend(list(com))
# l = [list(i) for i in l]
# print(l)