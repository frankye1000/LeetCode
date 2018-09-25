A = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [10,11,12]]


B = [[0 for i in range(len(A))] for r in range(len(A[0]))]
for i in range(len(B)):
    for j in range(len(B[0])):
        B[i][j] = A[j][i]

print(B)


