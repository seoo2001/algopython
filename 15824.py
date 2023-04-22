N = int(input())
ns = list(map(int, input().split()))
ns.sort()
nsum = [0]+ns[:]
for i in range(1,N+1): nsum[i] += nsum[i-1]
D=1000000007

def square(x, k):
    a = 1
    while k>0:
        if k%2: a = (a*x)%D; k-=1
        x = (x*x)%D; k//=2
    return a%D

def calsum(s,e): return nsum[e+1]-nsum[s]
ans = 0
for i in range(1,N):
    ans = (ans+(calsum(i,N-1)-calsum(0,N-1-i))*square(2,i-1))%D
print(ans)