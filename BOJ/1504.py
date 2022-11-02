import sys, heapq
nodenum, trunknum = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(nodenum+1)]
for _ in range(trunknum):
  v, w, c = map(int, sys.stdin.readline().split())
  graph[v].append([w, c])
  graph[w].append([v, c])
node1, node2 = map(int, sys.stdin.readline().split())

def dijk(s, e):
  visited = [10**7 for _ in range(nodenum+1)]
  q = [[0, s]]
  while q:
    time, node = heapq.heappop(q)
    if node == e: return time
    if visited[node] <= time: continue
    visited[node] = time
    for nextnode, u in graph[node]:
      heapq.heappush(q, [time+u, nextnode])
  return 10**7
ans = min(dijk(1, node1)+dijk(node1, node2)+dijk(node2, nodenum), 
          dijk(1, node2)+dijk(node2, node1)+dijk(node1, nodenum))
if ans >= 10**7: print("-1")
else: print(ans)