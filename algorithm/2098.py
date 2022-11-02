import sys
rl = sys.stdin.readline
n = int(rl())
graph = [list(map(int, rl().split())) for _ in range(n)]
q = [(0,0,0)] # 현재까지 시간 합, 현재 위치, 지나온 도시들
dp = [[(10**6)*n]*(1<<n) for _ in range(n)] # 현재 위치, 이전까지 지나온 도시
dp[0][0] = 0
ans = (10**6)*n
while q:
  wsum, loc, visited = q.pop()
  if wsum > ans: continue
  if visited==int("0b"+"1"*(n-1)+"0", 2) and graph[loc][0]!=0:
    ans = min(ans, wsum+graph[loc][0])
    continue
  for i in range(1, n):
    if graph[loc][i] != 0 and visited|(1<<i)!=visited:
      k = visited|(1<<i)
      if dp[i][k] > wsum+graph[loc][i]:
        dp[i][k] = wsum+graph[loc][i]
        q.append((wsum+graph[loc][i], i, k))
print(ans)