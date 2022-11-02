N = int(input())
ans = [0 for _ in range(10)]
point = 1
while N:
  if N%10 != 9:
    a = N
    while a:
      ans[a%10] += point
      a//=10
    N -= 1
    if N == 0: break
  else:
    for i in range(10):
      ans[i] += point*(((N//10))+1)
    ans[0] -= point
    point *= 10
    N//=10
print(' '.join(map(str, ans)))