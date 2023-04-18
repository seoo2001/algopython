import sys
rl = sys.stdin.readline
N = int(rl())
ns = list(map(int, rl().split()))
a, b = [], []

for i in range(1,N):
    if ns[i]%2==0: a.append(ns[i])
    else: b.append(ns[i])
if ns[0]%2==1: a,b=b,a

prime = [1 for _ in range(2001)]
prime[0], prime[1] = 0, 0
for i in range(2,2001):
    if not prime[i]: continue
    j = i*i
    while True:
        if j>2000:break
        prime[j] = 0; j+=i

g = [[] for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b)):
        if prime[a[i]+b[j]]: g[i].append(j)

def dfs(x):
    if x==-2: return False
    for i in g[x]:
        if v[i]: continue
        v[i] = 1
        if slt[i]==-1 or dfs(slt[i]):
            slt[i] = x
            return True
    return False

ans = []
for i in range(len(b)):
    if prime[b[i]+ns[0]]==0: continue
    slt = [-1 for _ in range(len(b))]
    slt[i] = -2
    pair = 0
    for j in range(len(a)):
        v = [0 for _ in range(len(b))]
        if dfs(j): pair+=1
    if pair==len(a): ans.append(b[i])
if ans and len(b)==N//2: print(*sorted(ans))
else: print(-1)