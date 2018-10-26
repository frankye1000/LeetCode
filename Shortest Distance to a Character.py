S = "loveleetcode"
C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Cindex = [i for i, v in enumerate(S) if v == C]
print([min([abs(i - j) for j in Cindex]) for i in range(len(S))])
