A = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

even = [v for v in A if v%2 == 0]
odd = [v  for v in A if v%2 ==1]

r = []
for i in range(len(even)):
    r.append(even[i])
    r.append(odd[i])
print(r)
