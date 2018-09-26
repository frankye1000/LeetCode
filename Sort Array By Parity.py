A = [3,1,2,4]
# 時間複雜度有問題
# even_index = [_ for _ in range(len(A)) if A[_]%2==0]
#
# for k in range(len(even_index)):
#
#     s_index = even_index[k]
#     print(s_index)
#     while A[s_index-1]%2 != 0 :
#         if s_index == 0 :
#             break
#         A[s_index-1],A[s_index] = A[s_index],A[s_index-1]
#         print(A)
#         s_index = s_index-1

# 作弊方法
# B=[]
# for i in range(len(A)):
#     if A[i]%2==0 :
#         B = [A[i]]+B
#     else:
#         B.append(A[i])

# 解答
i, j = 0, len(A) - 1
while i < j:
    if A[i] % 2 > A[j] % 2:
        A[i], A[j] = A[j], A[i]
        print(A)

    if A[i] % 2 == 0:
        i += 1
        print(A)
    if A[j] % 2 == 1:
        j -= 1
        print(A)


