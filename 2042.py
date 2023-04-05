import sys
rl = sys.stdin.readline
N, M, K = map(int, rl().split())
ns = [int(rl()) for _ in range(N)]
tree = [0]*(N*4)
def makeSegTree(start, end, node):
    if start==end:
        tree[node] = ns[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = makeSegTree(start, mid, node*2)+makeSegTree(mid+1, end,node*2+1)
    return tree[node]

makeSegTree(0,N-1,1)

def calSum(start, end, node, left, right):
    if left > end or right < start: return 0
    if left<=start and end<=right: return tree[node]
    mid = (start+end)//2
    return calSum(start,mid,node*2,left,right)+calSum(mid+1,end,node*2+1,left,right)

def update(start, end, node, idx, w):
    if idx<start or idx>end: return
    tree[node]+=w
    if start==end: return
    mid = (start+end)//2
    update(start,mid,node*2,idx,w)
    update(mid+1,end,node*2+1,idx,w)

for _ in range(M+K):
    a, b, c = map(int, rl().split())
    if a==1:
        update(0,N-1,1,b-1,c-ns[b-1])
        ns[b-1] = c
    else:
        print(calSum(0,N-1,1,b-1,c-1))