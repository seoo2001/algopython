import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(rl())
   
def makeRow(pre, h):
    seat = [1 for _ in range(W)]
    for i in range(W):
        if pre[i] == 1:
            if i != 0: seat[i-1] = 0
            if i !=W-1: seat[i+1] = 0
        if m[h][i] == "x": seat[i] = 0
    out = []
    def dfs(n,l):
        if n==W: out.append(l); return
        if not l:
            if seat[n]: dfs(n+1,l+[1])
        elif l[-1]==0 and seat[n]: dfs(n+1,l+[1])
        dfs(n+1,l+[0])
    dfs(0,[])
    return out

def makeV(l):
    out = 0
    for i, x in enumerate(l):
        if x: out += 2**i
    return out

def cal(pre, v, h):
    if h == H: return 0
    if dp[h][v] != -1: return dp[h][v]
    dp[h][v] = 0
    q = makeRow(pre,h)
    for qq in q:
        dp[h][v] = max(dp[h][v], cal(qq,makeV(qq),h+1)+sum(qq))
    return dp[h][v]

for _ in range(N):
    H, W = map(int, input().split())
    m = [list(input()) for _ in range(H)]
    dp = [[-1]*(2**W) for _ in range(H)]
    print(cal([0]*W, 0, 0))