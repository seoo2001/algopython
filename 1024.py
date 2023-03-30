n, l = map(int, input().split())
s = 0
while l<101:
    if l%2==1:
        if n%l == 0: 
            s = n/l-l//2
            break
    else:
        if n%(l/2) == 0 and (n//(l/2))%2==1:
            s = n//(l/2)/2-(l/2)+1
            break
    l+=1
if l==101 or s <0: print(-1)
else:
    for i in range(l):
        print(int(s), end = " ")
        s+=1