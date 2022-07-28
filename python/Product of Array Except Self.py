# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#########################################
## 時間複雜度超過
# nums=[1,2,3,4]

# out=[]
# for i in range(len(nums)):
#     l = nums[:i]+nums[i+1:]
#     n = 1
#     for j in l:
#         n = n*j
#     out.append(n)
##########################################
## 空間複雜度超過
# nums = [1, 2, 3, 4]
# all=[]
# for i in range(len(nums)):
#     l = nums[:i]+nums[i+1:]
#     all.extend(l)
# print(all)
#
# output=[]
# out=1
# count=0
# for k in all:
#     out = out*k
#     count=count+1
#     if count%(len(nums)-1) == 0:
#         output.append(out)
#         count=0
#         out=1
#
# print(output)
#############################################
## 時間複雜度超過
# nums = [1,2,3,4]
# twonums = (nums+nums)[1:-1]
# print(twonums)
#
# out=[]
#
# for i in range(len(twonums)-len(nums)+2):
#     n=1
#     for j in twonums[i:i+len(nums)-1]:
#         n=n*j
#     out.append(n)
#
# print(out)
#############################################
## 解答

nums = [2,3,4,5]
size = len(nums)
output = [1] * size
print(output)

left = 1
for x in range(size - 1):
	left *= nums[x]
	output[x + 1] *= left

print(output)
right = 1
for x in range(size - 1, 0, -1):

	right *= nums[x]

	output[x - 1] *= right

print(output)


