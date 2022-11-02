import sys

rl = sys.stdin.readline
n = int(rl())
gh = [list(int(x) for x in rl().rstrip()) for _ in range(n)]
ch, ans = 0, 0
q = []
q.append([[0], 0])
dp = [[10]*(2**15) for _ in range(n)]
while q:
    xs, ch = q.pop()
    k = "0b"+"".join(["1" if i in xs else "0" for i in range(n)])
    if dp[xs[-1]][int(k, 2)] <= ch: continue 
    dp[xs[-1]][int(k, 2)] = ch
    ans = max(ans, len(xs))
    for i, next in enumerate(gh[xs[-1]]):
        if next >= ch and i not in xs:
            q.append([xs+[i], next])
print(ans)