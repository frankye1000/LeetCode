nums = [1,2,3]
k = 3
# Output: 5
## Memory Limit Exceeded
# combin = []
# for j in range(len(nums)):
#     for i in range(1, len(nums)-j+1):
#         combin.append(nums[j:j+i])
#
#
# l = [sum(i) for i in combin]
# r = 0
# for j in l:
#     if j == k:
#         r += 1
# print(r)

def summ(n):
    if k == 0:
        return

