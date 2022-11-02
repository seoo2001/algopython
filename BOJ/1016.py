import sys
n, m = map(int, sys.stdin.readline().split())

def check(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0: return False
  return True

case = []
i = 2
while True:
  if i**2 > m: break
  if check(i): case.append(i**2)
  i += 1

answer = [1 for _ in range(1, m-n+1)]
for c in case:
  t = n//c
  while True:
    if c*t > m: break
    elif c*t in answer:
      answer.remove(c*t)
    t += 1
print(sum(answer))