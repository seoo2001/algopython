import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
N, L = map(int, rl().split())
q = [int(rl()) for _ in range(N)]
if L not in q: q.append(L); N+=1
q.sort()
dp = [[[-1,-1] for _ in range(N+1)] for _ in range(N+1)]

def cal(l,r,f, idx):
    if l==0 and r==N-1: return 0
    if dp[l][r][f] != -1: return dp[l][r][f]
    s = r if f else l
    lmin = 1e9 if l==0 else cal(l-1,r,0,idx-1)+(q[s]-q[l-1])*idx
    rmin = 1e9 if r==N-1 else cal(l,r+1,1,idx-1)+(q[r+1]-q[s])*idx
    dp[l][r][f] = min(lmin, rmin)
    return dp[l][r][f]

start = q.index(L)
print(cal(start,start,0,N-1))