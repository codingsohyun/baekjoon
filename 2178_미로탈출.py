from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 #이동할 때 지나야하는 최소 칸수를 더함

    return graph[n - 1][m - 1] # graph[n - 1][m - 1]에는 최소 칸 수의 최종값이 들어가게 된다.


print(bfs(0, 0))

#1. graph[0][0]부터 (실제 위치는 (1, 1)) bfs를 이용해 동, 서, 남, 북을 검사하여 이동했을 때 1인 값을 찾는다.
-> 값이 1 이어야 이동할 수 있기 때문에
2. 만약 1이라면 그 전 값에 +1을 하여 이동할 때 지나야 하는 최소 칸 수를 더해준다.
3. 이렇게 쭉 검사 하다보면 마지막 graph[n - 1][m - 1]에는 최소 칸 수의 최종값이 들어가게 된다.
