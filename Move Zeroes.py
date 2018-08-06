# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

##############################################################
# nums = [1, 2, 0, 3, 12, 0, 15]
# count=0
# for i in nums:
#     if i == 0:
#         count+=1
# for j in range(count):
#     for i in range(len(nums)-1):
#         if nums[i] == 0:
#
#             nums[i],nums[i+1] = nums[i+1],nums[i] #swap
#             print(nums)


##############################################################
# nums = [0,1,0,3,12]
# for i in nums:
#     if i == 0:
#         nums.remove(i)
#         nums.append(0)
#
# print(nums)

##############################################################
##Kent哥解答
nums = [1, 2, 0, 3, 12, 0, 15]
for i in range(len(nums)):  # find the first 0
    if nums[i] == 0:
        t = i
        break

for i in range(t + 1, len(nums)):
    if nums[i] != 0:
        nums[t] = nums[i]
        t = t + 1

for i in range(t, len(nums)):  # padding zeros
    nums[i] = 0

print(nums)


