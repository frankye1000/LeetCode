# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]

# matrix = [
#   [1,9],
#   [2,1],
#   [3,2],
#   [4,3]
# ]

matrix = [[83],[64],[57]]

m = len(matrix)-1
n = len(matrix[0])-1

if m==0 or n==0:
    print(True)
else:
    temp=[]
    for m1 in range(m):
        for n1 in range(n):
            temp.append(matrix[m1][n1]==matrix[m1+1][n1+1])
    if len(set(temp))==1:
        print(temp[0])
    else:
        print(False)