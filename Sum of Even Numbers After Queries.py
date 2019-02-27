"""We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.



Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation:
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4."""

A = [1]
queries = [[4, 0]]

S = sum([i for i in A if i % 2 == 0])
for query in queries:
    adds = query[0]
    index = query[1]
    #兩個都奇數
    if A[index] % 2 != 0 and adds % 2 != 0:
        S += A[index] + adds

    #兩個都偶數
    elif A[index] % 2 == 0 and adds % 2 == 0:
        S += adds

    #偶數 奇數
    elif A[index] % 2 == 0 and adds % 2 != 0:
        S -= A[index]

    #奇數 偶數
    A[index] = A[index] + adds
    print(S)



# Time Limit Exceeded
# re = []
# for query in queries:
#     adds = query[0]
#     index = query[1]
#     A[index] = A[index] + adds
#
#     even = [i for i in A if i % 2 == 0]
#
#     re.append(sum(even))
# print(re)