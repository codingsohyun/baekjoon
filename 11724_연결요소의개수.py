import sys
sys.setrecursionlimit(10**6) #파이썬의 재귀 최대 깊이 설정 (런타임 에러 방지)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split()) #정점의 개수 n, 간선의 개수 m

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (n+1) #방문하지 않음으로 초기화
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count) #연결 요소의 개수