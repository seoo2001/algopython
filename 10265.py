import sys
rl = sys.stdin.readline
N, K = map(int, input().split())
q = list(map(int, input().split()))
g = [[] for _ in range(N+1)]
grev = [[] for _ in range(N+1)]
for i, x in enumerate(q):
    g[i+1].append(x)
    grev[x].append(i+1)

#make stack
v = [0]*(N+1)
stack = []
def DFS(n):
    if v[n]: return
    v[n] = 1
    for t in g[n]: DFS(t)
    stack.append(n)

for i in range(1,N+1): DFS(i)

#make scc
v = [0]*(N+1)
sccLabel = [i for i in range(N+1)]
def makeScc(n, root):
    if v[n]: return
    v[n] = 1
    sccLabel[n] = root
    for t in grev[n]:
        makeScc(t, root)
while stack:
    t = stack.pop()
    makeScc(t,t)

print(sccLabel)
sccSize = []



dp = [0 for _ in range(N)]