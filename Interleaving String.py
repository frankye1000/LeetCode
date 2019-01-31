"""Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false"""

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

if len(s2) + len(s1) != len(s3):
    print(False)
res = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
# 代表從s1中取''，從s2中取''的情况
res[0][0] = 1
for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        if i == 0 and j == 0:
            continue
        # 代表從s1中取''，從s2中不取''的情况
        elif i == 0:
            res[i][j] = res[i][j - 1] & (s2[j - 1] == s3[j - 1])
        # 代表從s2中取''，從s1中不取''的情况
        elif j == 0:
            res[i][j] = res[i - 1][j] & (s1[i - 1] == s3[i - 1])
        # 代表從s1中不取''，從s2中不取''的情况
        else:
            res[i][j] = (res[i - 1][j] & (s1[i - 1] == s3[i + j - 1])) or (res[i][j - 1] & (s2[j - 1] == s3[i + j - 1]))
print(bool(res[len(s1)][len(s2)]))