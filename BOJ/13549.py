import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
visit = [100001 for _ in range(100001)]
q = [[0, n]]
ans = 0
while q:
  time, dis = heapq.heappop(q)
  if dis > 100000 or dis<0: continue
  if visit[dis] <= time: continue
  visit[dis] = time
  if dis == m:
    ans = time
    break
  heapq.heappush(q, [time, dis*2])
  heapq.heappush(q, [time+1, dis+1])
  heapq.heappush(q, [time+1, dis-1])
print(ans)