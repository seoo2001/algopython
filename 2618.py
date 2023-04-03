import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline
N = int(rl())
W = int(rl())
q = [[1,1],[N,N]]
for _ in range(W): q.append(list(map(int, rl().split())))
W+=2
dp = [[-1 for _ in range(W)] for _ in range(W)]
def cal(s1, s2):
    if s1==W-1 or s2==W-1: return 0
    if dp[s1][s2] != -1: return dp[s1][s2]
    dp[s1][s2] = 1e9
    sm = max(s1,s2)+1
    s1t = cal(sm, s2)+abs(q[s1][0]-q[sm][0])+abs(q[s1][1]-q[sm][1])
    s2t = cal(s1, sm)+abs(q[s2][0]-q[sm][0])+abs(q[s2][1]-q[sm][1])
    dp[s1][s2] = min(s1t, s2t)
    return dp[s1][s2]

def makeRoute(s1, s2):
    if s1==W-1 or s2==W-1: return
    sm = max(s1,s2)+1
    s1t = cal(sm, s2)+abs(q[s1][0]-q[sm][0])+abs(q[s1][1]-q[sm][1])
    s2t = cal(s1, sm)+abs(q[s2][0]-q[sm][0])+abs(q[s2][1]-q[sm][1])
    if s1t < s2t:
        print(1)
        makeRoute(sm,s2)
    else:
        print(2)
        makeRoute(s1,sm)

print(cal(0,1))
makeRoute(0,1)