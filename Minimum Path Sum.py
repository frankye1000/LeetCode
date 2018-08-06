import numpy as np
l = [[1,3,1],[1,5,1],[4,2,1],[2,9,1]]
m = len(l)
n = len(l[0])

# 先把第一列算出來
for r in range(1,n):
    l[0][r] = l[0][r]+l[0][r-1] #自己加上左邊一個
# 先把第一行算出來
for c in range(1,m):
    l[c][0] = l[c][0]+l[c-1][0] #自己加上上面一個

# 算中間
for i in range(1,m):
    for j in range(1,n):
        l[i][j] = min(l[i][j]+l[i-1][j] , l[i][j]+l[i][j-1])
print(l[m-1][n-1])