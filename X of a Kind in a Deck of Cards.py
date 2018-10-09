deck = [1,1,1,1,2,2,2,2,2,2,5,5,5]

element = list(set(deck))

g=[]
for j in range(len(element)):
    temp=[]
    for i in range(len(deck)):
        if element[j]==deck[i]:
            temp.append(deck[i])
    g.append(temp)

length = [len(g[i]) for i in range(len(g))]
print(length)
# 找有沒有公因數
def gcd(x,y):
    while (y):
        x,y = y, x%y
    return x

min_ = min(length)
print(min_)

gcdre = [gcd(min_,length[i]) for i in range(len(length))]
for i in range(len(gcdre)):
    if gcdre[i] == 1:
        print(False)
    else:
        print(True)


