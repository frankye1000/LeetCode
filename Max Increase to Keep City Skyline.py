grid = [[3,0,8,4],
        [2,4,5,7],
        [9,2,6,3],
        [0,3,1,0]]

leftright = [max(grid[i]) for i in range(len(grid))]
# topbottom = []
# for i in range(len(grid)):
#     temp=[]
#     for j in range(len(grid)):
#         temp.append(grid[j][i])
#     topbottom.append(max(temp))

topbottom = [max([grid[j][i] for j in range(len(grid))]) for i in range(len(grid))]

finalbuilding = [[min(leftright[i],topbottom[j]) for j in range(len(topbottom))] for i in range(len(leftright))]

count=0
for i in range(len(grid)):
    for j in range(len(grid)):
        count += finalbuilding[j][i] - grid[j][i]
print(count)