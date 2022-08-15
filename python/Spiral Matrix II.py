n = 5
matrix = [[0]*n for i in range(n)]
print(matrix)

loop = n//2
mid  = n//2
startx, starty = 0, 0
step = n-1
number = 1

for i in range(loop):  # 控制要loop幾次
    for s in range(step):                   # 控制要前進幾格
        matrix[startx][starty] = number     # 左至右
        starty+=1
        number+=1
    for s in range(step):                   # 控制要前進幾格
        matrix[startx][starty] = number     # 上至下     
        startx+=1
        number+=1
    for s in range(step):                   # 控制要前進幾格
        matrix[startx][starty] = number     # 右至左     
        starty-=1
        number+=1  
    for s in range(step):                   # 控制要前進幾格
        matrix[startx][starty] = number     # 下至上     
        startx-=1
        number+=1

    startx += 1 
    starty += 1
    step -= 2

if n%2 != 0: # n=奇數
    matrix[mid][mid]=number
print(matrix)