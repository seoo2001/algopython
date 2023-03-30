import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
n = int(rl())
nowl = list(map(int, rl().rstrip()))+[0,0,0,0,0]
nxtl = list(map(int, rl().rstrip()))+[0,0,0,0,0]
dp = [[[[-1 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(n+5)]
def per10(x): return (x+10)%10
def cal(idx, x, y, z):
    if idx==n: return 0
    if dp[idx][x][y][z] != -1: return dp[idx][x][y][z]
    dp[idx][x][y][z] = 1e9
    for t, i in enumerate([per10(nxtl[idx]-x), per10(x-nxtl[idx])]):
        for j in range(i+1):
            for k in range(j+1):
                if t == 0: ny, nz = per10(y+j), per10(z+k)
                else: ny, nz = per10(y-j), per10(z-k)
                dp[idx][x][y][z] = min(dp[idx][x][y][z], cal(idx+1, ny, nz, nowl[idx+3]) + (i-j+2)//3 + (j-k+2)//3 + (k+2)//3)
    return dp[idx][x][y][z]

print(cal(0,nowl[0],nowl[1],nowl[2]))