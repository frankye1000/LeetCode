
class Solution(object):
    def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):  # 從中間向左遍歷
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):  # 從中間向右遍歷
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))

    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

#################################################################
#以下為暴力解

# sum_list=[]
# for i in range(len(nums)):
#     for j in range(1,len(nums)-i+1):
#         sum_list.append(sum(nums[i:i+j]))
#
# print(max(sum_list))