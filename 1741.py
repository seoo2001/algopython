import sys
rl = sys.stdin.readline
n, m = map(int, rl().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, rl().split())
    g[a].append(b)
    g[b].append(a)

p = [i for i in range(n+1)]
sz = [1 for _ in range(n+1)]
def findP(x):
    if p[x]==x: return x
    p[x] = findP(p[x])
    return p[x]

def join(a,b):
    a = findP(a)
    b = findP(b)
    if a > b: a, b = b, a
    if a==b: return
    p[b] = a
    sz[a] += sz[b]

def bsearch(x, l):
    s, e = 0, len(l)-1
    while(s<=e):
        mid = (s+e)//2
        if l[mid]==x: return True
        elif l[mid]>x: e = mid-1
        else: s = mid+1
    return False

minNode = 1
for i in range(1,n+1):
    g[i].sort()
    if len(g[i]) < len(g[minNode]): minNode = i

aa, bb = [], []
for i in range(1,n+1):
    if not bsearch(i, g[minNode]):
        join(i, minNode)
        bb.append(i)
    else: aa.append(i)

for i in aa:
    for j in bb:
        if not bsearch(j,g[i]): join(i,j)
    for k in aa:
        if not bsearch(k,g[i]): join(i,k)
ans = [sz[i] for i in range(1,n+1) if p[i]==i]
ans.sort()
print(len(ans))
print(*ans)