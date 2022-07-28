import math
x = 1
y = 4
def BinaryExpansion(y):
    binary = []
    while y != 1:
        if y==0:
            return [0]
        else:
            q = int(y/2) #商
            r = y%2 #餘數
            binary.append(r)
            y = q

    binary = [1] + binary[::-1]
    return binary

b = BinaryExpansion(y)

x = BinaryExpansion(x)
y = BinaryExpansion(y)

long = max(len(x),len(y))
x = [0]*(long-len(x))+x
y = [0]*(long-len(y))+y


hammingDistance=0
for i in range(long):
    if x[i]!=y[i]:
        hammingDistance+=1
print(hammingDistance)