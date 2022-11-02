import sys, heapq
nodenum, trunknum = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(nodenum+1)]
for _ in range(trunknum):
  v, w, u = map(int, sys.stdin.readline().split())
  graph[v].append([w, u])
  graph[w].append([v, u])

visited = [1e9] * (nodenum+1)
visited[1] = 0
q = []
heapq.heappush(q, [0, 1])
while q:
  time, node = heapq.heappop(q)
  if visited[node] < time: continue
  for nextnode, u in graph[node]:
    nexttime = time + u * 2
    if nexttime < visited[nextnode]:
      visited[nextnode] = nexttime
      heapq.heappush(q, [nexttime, nextnode])

visited2 = [[1e9 for _ in range(nodenum+1)] for _ in range(2)]
visited2[1][1] = 0
q2 = []
heapq.heappush(q2, [0, 1, False])
while q2:
  time, node, check = heapq.heappop(q2)
  if check and visited2[0][node] < time: continue
  if not check and visited2[1][node] < time: continue
  for nextnode, u in graph[node]:
    if check:
      nexttime = time + u * 4
      if nexttime < visited2[1][nextnode]:
        visited2[1][nextnode] = nexttime
        heapq.heappush(q2, [nexttime, nextnode, False])
    else:
      nexttime = time + u
      if nexttime < visited2[0][nextnode]:
        visited2[0][nextnode] = nexttime
        heapq.heappush(q2, [nexttime, nextnode, True])

ans = 0
for i in range(2, nodenum+1):
  if visited[i] < min(visited2[0][i], visited2[1][i]): ans += 1
print(ans)