"""We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.



Example 1:

Input: ["cba","daf","ghi"]
Output: 1
Explanation:
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:

Input: ["a","b"]
Output: 0
Explanation: D = {}
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}


Note:

1 <= A.length <= 100
1 <= A[i].length <= 1000"""

A = ["zyx", "wvu", "tsr"]

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_dict = {}
for i, letter in enumerate(letters):
    letter_dict[letter] = i

p = []
for j in range(len(A[0])):
    temp = []
    for i in range(len(A)):
        temp.append(letter_dict[A[i][j]])
    p.append(temp)
print(p)

count = 0
for i in p:
    temp = []
    for j in range(len(i) - 1):
        if i[j] - i[j+1]>0:
            temp.append(False)
        else:
            temp.append(True)

    if all(temp) == False:
        count += 1
print(count)