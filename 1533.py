N,S,E,T = map(int, input().split())
mod = 1000003
m = [[0]*N*5 for _ in range(N*5)]
for i in range(N):
    q = list(map(int, input()))
    for j in range(N):
        if q[j] == 0: continue
        m[i*5][j*5+q[j]-1] = 1
    for j in range(1,5):
        m[i*5+j][i*5+j-1] = 1

def sqMat(mat, mat0):
    out = [[0]*N*5 for _ in range(N*5)]
    for i in range(N*5):
        for j in range(N*5):
            for k in range(N*5):
                out[i][j] = (out[i][j]+mat[i][k]*mat0[k][j])%mod
    return out

def fpow(mat, n):
    if n == 1: return mat
    else:
        x = fpow(mat, n//2)
        if n % 2 == 0: return sqMat(x,x)
        else: return sqMat(sqMat(x,x),mat)

m = fpow(m ,T)
print(m[(S-1)*5][(E-1)*5])