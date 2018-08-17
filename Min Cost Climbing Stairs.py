# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].


# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [10, 15, 20]
# cost = [0,1,2,2]
# cost=[0,2,2,1]
cost=[0,2,3,2]


for i in range(2,len(cost)):
    l=cost[i] + cost[i-1]
    z=cost[i] + cost[i-2]
    m = min(l,z)
    cost[i]=m

print(min(cost[-1],cost[-2]))










# 錯誤答案
# cost0 = [0]+cost
# print(cost0)
#
# spend0=0
# i0=0
# while i0<len(cost0)-2:
#     if cost0[i0+1]>=cost0[i0+2]:
#         spend0 += cost0[i0+2]
#         i0+=2
#     else:
#         spend0 +=cost0[i0+1]
#         i0+=1
# print(spend0)
#
#
# cost.reverse()
# cost = [0]+cost
# print(cost)
# spend=0
# i=0
# while i <len(cost)-2:
#     if cost[i+1]>=cost[i+2]:
#         spend+=cost[i+2]
#         i+=2
#     else:
#         spend+=cost[i+1]
#         i+=1
# print(spend)
#
# print(min(spend0,spend))




