# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


def permute(self, nums):
    if len(nums) <= 1:
        return [nums]

    res = []
    for i, x in enumerate(nums):
        for elem in self.permute(nums[:i] + nums[i + 1:]):
            res.append([x] + elem)

    return res


############################################
##Kent哥解答
def insert_p(arr, a):
    t = []
    for i in range(len(arr) + 1):
        t.append(arr[:i] + [a] + arr[i:])
    return t


def perm(x):
    if len(x) == 1:
        return [x]
    else:
        t = []
        for p in perm(x[1:]):
            t.extend(insert_p(p, x[0]))
        return t


print(perm([1, 2, 3]))


