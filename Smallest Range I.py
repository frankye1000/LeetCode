A = [1,3,6]
K = 3

Max=max(A)
Min=min(A)
# 看有沒有交集

if Min+K < Max-K:
    print(Max-K-(Min+K))
else:
    print(0)