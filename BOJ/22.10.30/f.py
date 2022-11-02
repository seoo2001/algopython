n, k = map(int, input().split())
case = [list(input().split()) for _ in range(n)]
q = [(0,0,0)]
for r, d in case:
  x, y, sumd = q[-1]
  d = int(d)
  sumd += d
  if r == "N": q.append((x, y-d,sumd))
  elif r == "W": q.append((x-d, y,sumd))
  elif r == "S": q.append((x, y+d,sumd))
  elif r == "E": q.append((x+d, y,sumd))
print(q)
