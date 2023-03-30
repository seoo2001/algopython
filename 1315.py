import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
n = int(rl())
qs = [list(map(int, rl().split()))+[i] for i in range(n)]
qstr, qint = qs[:], qs[:]
qstr.sort(key = lambda x : x[0])
qint.sort(key = lambda x : x[1])
dp = [[-1 for _ in range(1001)] for _ in range(1001)]
visit = [0 for _ in range(n)]

def cal(str_, int_, visit, sidx, iidx):
    if str_ >= 1000 or int_ >= 1000 or sidx==n or iidx==n: return 51
    if dp[str_][int_] != -1: return dp[str_][int_]
    v = []
    left,leftn = 0,0
    while True:
        if qstr[sidx][0] <= str_:
            if visit[qstr[sidx][3]] == 0:
                left += qstr[sidx][2]
                leftn += 1
                visit[qstr[sidx][3]] = 1
                v.append(qstr[sidx][3])
            sidx+=1
            if sidx==n: break
        else: break
    while True:
        if qint[iidx][1] <= int_:
            if visit[qint[iidx][3]] == 0:
                left += qint[iidx][2]
                leftn += 1
                visit[qint[iidx][3]] = 1
                v.append(qint[iidx][3])
            iidx+=1
            if iidx==n: break
        else: break
    if left == 0: return 0
    for i in range(left+1): dp[str_][int_] = max(dp[str_][int_], leftn+cal(str_+left-i, int_+i, visit, sidx, iidx))
    for x in v: visit[x] = 0
    return dp[str_][int_]

ans = cal(1,1,visit,0,0)
if ans > 50: print(n)
else: print(ans)