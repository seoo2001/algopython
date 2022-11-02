import sys, heapq
rl = sys.stdin.readline

node, trunk, k = map(int, rl().split())
graph = [[] for _ in range(node+1)]
for _ in range(trunk):
  v, w, u = map(int, rl().split())
  graph[v].append([w, u])

dp = [[10**9] * k for _ in range(node+1)]
q = [[0, 1]]
dp[1][0] = 0
while q:
  d, n = heapq.heappop(q)

  for nn, u in graph[n]:
    nd = d + u
    if dp[nn][k-1] > nd:
      dp[nn][k-1] = nd
      dp[nn].sort()
      heapq.heappush(q, [nd, nn])

for i in range(1, node+1):
  if dp[i][k-1] == 10**9: print("-1")
  else: print(dp[i][-1])