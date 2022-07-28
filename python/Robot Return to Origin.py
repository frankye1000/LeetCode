moves = "RRDD"
# Output: true

start = [0, 0]

for i in moves:
    if i == "R":
        start[1] += 1
    elif i == "L":
        start[1] -= 1
    elif i == "U":
        start[0] += 1
    else:
        start[0] -= 1
if start[0] == 0 and start[1] == 0:
    print(True)
else:
    print(False)