"""A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts."""
import itertools

S = "ababcbacadefegdehijhklij"

# def FindIndexCover(A):
#     indexlist = [i for i, v in enumerate(S) if v == A]
#     Head = indexlist[0]
#     Tail = indexlist[-1]
#     cover = [i for i in range(Head, Tail + 1)]
#     return cover
#
# key = list(set(S))
# print('key = ', key)
# dic = {}
# for i in key:
#     dic[i] = FindIndexCover(i)
# print('dict = ', dic)
#
# # comb = list(itertools.combinations(key, 2))
# # print('combination = ', comb)
#
# def CoverWhich(A):
#     coverlist = []
#     elsekeys = [_ for _ in key if _ != A]
#     for j in elsekeys:
#         if any([id in dic[A] for id in dic[j]]):
#             coverlist.append(j)
#
#     return coverlist
#
# coverdic = {}
# for i in key:
#     coverdic[i] = CoverWhich(i)
#
# for k in key:
#     key.remove(k)
#     for value in coverdic[k]:
#         for v in value:
#             print(coverdic[v])
#             print(v)
#             key.remove(v)
#     print('*************')



lindex = {c: i for i, c in enumerate(S)}
print(lindex)
j = anchor = 0
ans = []
for i, c in enumerate(S):
    j = max(j, lindex[c])
    print(i, j)

    if i == j:
        ans.append(j - anchor + 1)
        anchor = j + 1
# print(ans)
