A = "this apple is sweet"
B = "this apple is sour"
# Output: ["sweet","sour"]

A = A.split(" ")
B = B.split(" ")

C = A + B
print(C)
dictC={}
for i in C:
    if i not in dictC:
        dictC[i] = 1
    else:
        dictC[i] += 1
r=[]
for j in dictC:
    if dictC[j] == 1:
        r.append(j)
print(r)