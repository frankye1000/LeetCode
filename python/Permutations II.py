def insert_p(arr,a):
    t=[]
    for i in range(len(arr)+1):
        t.append(arr[:i]+[a]+arr[i:])
    return t

def perm(x):
    if len(x) <=1:
        return [x]
    else:
        r=[]
        for p in perm(x[1:]):

            # print(insert_p(p,x[0]))
            r.extend(insert_p(p,x[0]))
        r2=[]
        for i in r:
            if i not in r2:
                r2.append(i)
        return r2

print(perm([1,1,2]))