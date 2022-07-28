"""Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""

A = [-4, 0]
A = [i**2 for i in A]

# Time Limit Exceeded
# def bubblesort(A):
#     for j in range(len(A)):
#         for i in range(len(A)-1):
#             if A[i] > A[i+1]:
#                 A[i], A[i+1] = A[i+1], A[i]
#     return A

print(sorted(A))

