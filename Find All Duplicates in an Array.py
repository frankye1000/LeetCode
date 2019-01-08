"""Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]"""

nums = [4, 3, 2, 7, 8, 2, 3, 1]
## method1 Time Limit Exceeded
# r = []
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j]:
#             r.append(nums[j])

## method2 extra space Exceeded
# nums = sorted(nums)
# r = [nums[i] for i in range(len(nums) - 1) if nums[i] == nums[i + 1]]
# print(r)

## answer
res = []
for x in nums:
    print("x = ", x)
    if nums[abs(x) - 1] < 0:
        res.append(abs(x))
        print(nums)

    else:

        nums[abs(x) - 1] *= -1
        print(nums)
