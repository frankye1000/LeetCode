left = 1
right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def JudgeTF(digit):
    s = str(digit)
    B = []
    for d in s:
        if d == '0':
            B.append(False)
        else:
            B.append(digit % int(d) == 0)

    return all(B)

r = [digit for digit in range(left, right + 1) if JudgeTF(digit)]
print(r)

