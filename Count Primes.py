# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# 如果我要判斷小於n = 100的質數，如果 i^2 > 100 => i=11 ， 所以我們只需要判斷到11

##############################################################################################
# Time Limit Exceeded

# import copy
# n = 2
#
# l = [i for i in range(0,n)]
# end = int(round(n ** 0.5,0))+1
# l2 = copy.deepcopy(l)
# l2 = l2[2:]
#
# for i in range(2,end+1):
#     print(l[i*2:n+1:i])
#     for j in l[i*2:n+1:i]:
#         if j in l2:
#             l2.remove(j)
# print(l2)
###############################################################################################
## 厄拉多赛筛法(sieve of Eratosthenes)
n = 10
if n < 3:
    print(0)
primes = [True] * n
primes[0] = primes[1] = False
for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
        primes[i*i:n:i] = [False]*len(primes[i*i:n:i])

    print(primes)