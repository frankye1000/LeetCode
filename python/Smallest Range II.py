A = [2,8,9]
K = 3

p=[]
for i in range(len(A)):
    p.extend([A[i] - K, A[i] + K])

print(sorted(p))