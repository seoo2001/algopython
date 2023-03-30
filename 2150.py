import sys
sys.setrecursionlimit(10**6)
V,E=map(int,input().split())
q = [[] for _ in range(V+1)]
qrev = [[] for _ in range(V+1)]
for _ in range(E):
    a,b=map(int,input().split())
    q[a].append(b)
    qrev[b].append(a)
stack = []
v = [0]*(V+1)
def DFS(x):
    if v[x]: return
    v[x] = 1
    for t in q[x]: DFS(t)
    stack.append(x)

for x in range(1,V+1): DFS(x)

v = [0]*(V+1)
ans = [[] for _ in range(V+1)]
def makeScc(n, root):
    if v[n]: return
    v[n] = 1
    ans[root].append(n)
    for t in qrev[n]: makeScc(t, root)

while stack:
    x = stack.pop()
    makeScc(x,x)

ans = [x for x in ans if x]
ans.sort(key = lambda x: min(x))
print(len(ans))
for aa in ans: print(*sorted(aa), end=" -1\n")