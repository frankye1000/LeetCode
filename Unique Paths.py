# def insert_p(arr,a):
#     t=[]
#     for i in range(len(arr)+1):
#         t.append(arr[:i]+[a]+arr[i:])
#     return t
#
# def perm(x):
#     if len(x) <=1:
#         return [x]
#     else:
#         r=[]
#         for p in perm(x[1:]):
#
#             # print(insert_p(p,x[0]))
#             r.extend(insert_p(p,x[0]))
#         r2=[]
#         for i in r:
#             if i not in r2:
#                 r2.append(i)
#         return r2
#
# def uniquePaths(m, n):
#     """
#     :type m: int
#     :type n: int
#     :rtype: int
#     """
#     nums = []
#     for i in range(m - 1):
#         nums.append(0)
#     for j in range(n - 1):
#         nums.append(1)
#     return len(perm(nums))
#
# print(uniquePaths(7,5))
#################################################################

m=3
n=2
# 做出矩陣
zero_matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(m):
    zero_matrix[0][i]=1
for j in range(n):
    zero_matrix[j][0]=1
print("zero_matrix=", zero_matrix)

# 旁邊都是1，直接算中間
for j in range(1,m):
    for i in range(1,n):
        zero_matrix[i][j] = zero_matrix[i-1][j] + zero_matrix[i][j-1]

print(zero_matrix[n-1][m-1])


