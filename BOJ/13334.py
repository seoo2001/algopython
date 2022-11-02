import sys
from collections import deque
rl = sys.stdin.readline
n = int(rl())
lines = []
for i in range(n):
  x, y = map(int, rl().split())
  if x > y: x, y = y, x
  lines.append([x, y])
lines.sort(key = lambda x: (x[1], x[0]))
d = int(rl())
ans = 0
q = deque()
ans = 0
print(lines)
for x, y in lines:
  print(q)
  if y - d <= x:
    q.append(x)
  q = deque(sorted(q))
  while q:
    t = q.popleft()
    if t >= y-d:
      q.appendleft(t)
      break
  ans = max(ans, len(q))
print(ans)