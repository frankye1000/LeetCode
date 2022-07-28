# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# 時間複雜度超過
# def ClimbStairs(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#
#     else:
#         return ClimbStairs(n-1)+ClimbStairs(n-2)

n = 7
u = [1, 1]
for i in range(n - 1):
    temp = u[0] + u[1]
    u[0], u[1] = u[1], temp