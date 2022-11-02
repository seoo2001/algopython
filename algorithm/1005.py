import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

for _ in range(N):
    nodeNum, edgeNum = map(int, sys.stdin.readline().split())
    nodes = list(map(int, sys.stdin.readline().split()))
    nodes.insert(0, 0)
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(edgeNum)]
    lastNode = int(sys.stdin.readline())
    graph = [[] for _ in range(nodeNum+1)]
    for x, y in edges:
        graph[y].append(x)

    nvisit = [0 for _ in range(nodeNum+1)]
    nMax = [0 for _ in range(nodeNum+1)]

    def dfs(x):
        result = []
        if nvisit[x] != 0:
            return nMax[x]
        for nextnode in graph[x]:
            if graph[nextnode]:
                result.append(dfs(nextnode))
            else:
                result.append(nodes[nextnode])
        nvisit[x] = 1
        nMax[x] = max(result) + nodes[x]     
        return nMax[x]

    if not graph[lastNode]:
        print(nodes[lastNode])
    else: print(dfs(lastNode))