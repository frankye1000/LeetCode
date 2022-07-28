"""Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?"""
nums = [1,2,1,3,2,5]
d = {}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
print([i for i in d if d[i] == 1])
