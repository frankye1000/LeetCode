"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keys={}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                print([keys[target-nums[i]],i])
            if nums[i] not in keys:
                keys[nums[i]] = i

"""失敗
target=-8
nums=[-1,-2,-3,-4,-5]

new_nums=[]
for i,v in enumerate(nums):
    new_nums.append({i:v})

from itertools import combinations

all_index=[]
for i in range(1, len(new_nums)+1):
    combination = list(combinations(new_nums, i))
    # print(combination)
    for dicts in combination:
        # print(dicts)
        now = 0
        now_dict=[]
        for value in dicts:
            now += list(value.values())[0]
            now_dict.append(value)

        if now == target:
             all_index.append(now_dict)
print(all_index)
"""

