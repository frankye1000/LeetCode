"""Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]"""

nums = [4, 3, 2, 7, 8, 2, 3, 1]

# Runtime: 12360 ms, faster than 0.51% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# length = len(nums)
# nums = set(nums)
# re = [i for i in range(1, length+1)]
# for i in nums:
#     re.remove(i)
# print(re)


# Time Limit Exceeded
# print([i for i in range(1, len(nums)+1) if i not in nums])

# Answer
re = [0]*len(nums)
for i in nums:
    re[i-1] = 1
print([i+1 for i, v in enumerate(re) if v==0])