import numpy as np
# s1 = 'netbase solutions inc'
# s1 = '0'+s1
# s2 = 'basics'
# s2 = '1'+s2
# matrix = np.zeros((len(s2), len(s1)))
#
# reme = []
# for i in range(1, len(s2)):
#     for j in range(1, len(s1)):
#
#         if s2[i] == s1[j]:
#             reme.append((i, j))
#             if matrix[i-1][j] == matrix[i][j-1]:
#                 matrix[i][j] = matrix[i-1][j] + 1
#             else:
#                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
#         else:
#             matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
#
# print(matrix)
# print(matrix[len(s2)-1][len(s1)-1])
# print(reme)




#########################################
#############    解答    #################
#########################################
s1 = 'rsagqqs'
s2 = 'rxxs'


def findNextChar(mark, maxlen, currlen, i, j, posArray, downFlag):
    tmpArr = posArray[:]
    m, n = mark.shape
    if i == m or j == n:  # reach the end of the string
        if currlen == maxlen:
            posArray = tmpArr + [0] * (n - len(tmpArr))  # padding zeros
            print('>>>', posArray)  #######print the answer
    else:
        if mark[i][j] > currlen and mark[i][j] > i:
            tmpArr.append(mark[i][j])
            findNextChar(mark, maxlen, currlen + 1, i + 1, j + 1, tmpArr, 1)

        # go right
        if mark[i][j] != 0:
            findNextChar(mark, maxlen, currlen, i, j + 1, tmpArr[:-1] + [0], 0)
        else:
            findNextChar(mark, maxlen, currlen, i, j + 1, tmpArr + [0], 0)
        # go down
        if downFlag == 1:
            findNextChar(mark, maxlen, currlen, i + 1, j, tmpArr, 1)


def calculateLCS(s1, s2):
    ###assume s2 is longer
    if len(s1) > len(s2):
        s1, s2 = s2, s1  # swap
    m = len(s1)
    n = len(s2)
    matrix = np.zeros((m + 1, n + 1), dtype=int)  # DP table, 記錄最大substring的長度
    mark = np.zeros((m, n), dtype=int)  # 記錄字母相同的坐標位置

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # character match
                if matrix[i - 1][j] == matrix[i][j - 1]:
                    matrix[i][j] = matrix[i][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                mark[i - 1][j - 1] = i
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    maxSubstringLength = matrix[m][n]

    # 找出所有組合
    findNextChar(mark, maxSubstringLength, 0, 0, 0, [], 1)


calculateLCS(s1, s2)
