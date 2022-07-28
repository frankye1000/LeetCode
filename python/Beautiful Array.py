"""For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)



Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]"""
"""因為題目要求任意兩個數的平均數不能在他們中間，如果一個數字左邊都是奇數，右邊都是偶數，
那麼肯定這個數字的二倍是偶數，肯定不會存在A[k] * 2 = A[i] + A[j]。
若數組A滿足上面的條件，那麼很容易從線性關係中看出來，對於A中的每個元素做
[2 * i for i in A]後者[2 * i - 1 for i in A]依然滿足上面的條件。
所以我們從最簡單的1開始推導，構造奇數+偶數拼接在一起成為新的數組，然後繼續這個操作，就能使得得到的一直是滿足條件的數組。
最後當數組的長度滿足條件就結束。因為結果數組的長度是2的整數次方，所以最後要把結果中小於等於N的留下來就行了
"""


N = 5
res = [1]
while len(res) < N:
    res = [2 * i - 1 for i in res] + [2 * i for i in res]
    print(res)
print([i for i in res if i <= N])