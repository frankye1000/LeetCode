"""Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99"""

nums = [0,1,0,1,0,1,99]
d = {}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
for i in d:
    if d[i] == 1:
        print(i)