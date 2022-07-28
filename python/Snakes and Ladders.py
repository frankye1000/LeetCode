board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

# board=[[-1,-1],[-1,1]]

# board=[[-1,4,-1],
#        [6,2,6],
#        [-1,3,-1]]

l=[]
for i in range(-1,-len(board)-1,-1):
    print(i)
    if i%2 != 0:
        l.extend(board[i])
    else:
        l.extend(board[i][::-1])


path=0
j = 0
while j < len(l):
    if path > len(l):
        print("No limit")
        break
    
    if l[j] != -1:
        j = l[j]
        path+=1

        print("j:%s" % j, "path:%s" % path)
    else:
        j += 1
        path+=1
        print("j:%s" % j, "path:%s" % path)
