import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, rl().split())
q = [[] for _ in range(N*2+1)]
qrev = [[] for _ in range(N*2+1)]

for _ in range(M):
    a, b = map(int, rl().split())
    q[-a+N].append(b+N)
    q[-b+N].append(a+N)
    qrev[b+N].append(-a+N)
    qrev[a+N].append(-b+N)

stack = []
v = [0]*(N*2+1)
def DFS(x):
    if v[x]: return
    v[x] = 1
    for t in q[x]: DFS(t)
    stack.append(x)

for i in range(N*2+1):
    if i!=N: DFS(i)

v = [0]*(N*2+1)
ans = [[] for _ in range(N*2+1)]
def makeScc(n, root):
    if v[n]: return
    v[n] = 1
    ans[root].append(n-N)
    for t in qrev[n]: makeScc(t, root)

while stack:
    x = stack.pop()
    makeScc(x,x)
    
out = 1
for xs in ans:
    for x in xs:
        if -x in xs: out = 0; break
    if not out: break
print(out)