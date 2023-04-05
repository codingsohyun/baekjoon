# DFS

n = int(input())
net = int(input())
graph = [[] for i in range(n+1)]

visited=[0]*(n+1)

for i in range(net):
    # graph.append(list(map(int, input().split())))
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(net):
    visited[net]=1
    for nx in graph[net]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)