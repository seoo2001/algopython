import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, rl().split())
q = [int(rl()) for _ in range(N)]
tree = [[1e11,0] for _ in range(N*4)]

def init(start, end, node):
    if start==end:
        tree[node][0] = q[start]
        tree[node][1] = q[start]
        return q[start]
    mid = (start+end)//2
    init(start, mid, node*2)
    init(mid+1, end, node*2+1)
    tree[node][0] = min(tree[node*2][0], tree[node*2+1][0])
    tree[node][1] = max(tree[node*2][1], tree[node*2+1][1])
init(0,N-1,1)
print(tree)
def cal(start, end, node, left, right,f):
    if end < left or right < start: return 0 if f else 1e9
    elif left<=start and end<=right: return tree[node][f]
    mid = (start+end)//2
    if not f: return min(cal(start,mid,node*2,left,right,f),cal(mid+1,end,node*2+1,left,right,f))
    return max(cal(start,mid,node*2,left,right,f),cal(mid+1,end,node*2+1,left,right,f))
    
    
for _ in range(M):
    a, b = map(int, rl().split())
    print(cal(0,N-1,1,a-1,b-1,0), cal(0,N-1,1,a-1,b-1,1))