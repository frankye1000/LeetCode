from collections import deque

deck = [17,13,11,2,3,5,7]
q = deque([i for i in range(len(deck))])
indexes = []
while q:
    indexes.append(q.popleft())
    if q:
        q.append(q.popleft())

deck.sort()
res = [0] * len(deck)
for i, pos in enumerate(indexes):
    res[pos] = deck[i]

print(res)