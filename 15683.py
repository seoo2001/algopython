from itertools import product
from copy import deepcopy
H, W = map(int ,input().split())
mtemp = [list(map(int, input().split())) for _ in range(H)]
q = []
for i in range(H):
    for j in range(W):
        if mtemp[i][j] != 0 and mtemp[i][j] != 6: q.append((mtemp[i][j],j,i))
cc = {1: [0], 2:[0,2], 3:[0,1], 4:[0,1,2], 5:[0,1,2,3]}
dr = [(1,0),(0,1),(-1,0),(0,-1)]
def check(f, l):
    cn,x,y=l[0],l[1],l[2]
    for r in cc[cn]:
        dx, dy = dr[(r+f)%4][0], dr[(r+f)%4][1]
        for i in range(1, 10):
            if not(0<=x+dx*i<W and 0<=y+dy*i<H): break
            if m[y+dy*i][x+dx*i]==6: break
            m[y+dy*i][x+dx*i] = 9
ans = 64
for pp in product(range(4),repeat=len(q)):
    m = deepcopy(mtemp)
    for i, f in enumerate(pp): check(f, q[i])
    ans = min(ans, sum(m,[]).count(0))
print(ans)