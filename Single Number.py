"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""


d = {}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
# print(d)
for i in d:
    if d[i] == 1:
        print(i)