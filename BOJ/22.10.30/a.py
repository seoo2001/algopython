n, m = map(int,input().split())
case = list(map(int,input().split()))
breaker = False
while not breaker:
  for i in range(n):
    if case[i] < m:
      print(i+1)
      breaker = True
      break
    m+= 1