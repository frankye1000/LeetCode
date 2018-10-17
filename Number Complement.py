num = 5
# output : 2
r = ""
for i in bin(num)[2:]:
    if i == '0':
        r += '1'
    else:
        r += '0'
print(r)
print(int(r,2))