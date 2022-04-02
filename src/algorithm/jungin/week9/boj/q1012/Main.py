import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m, n = 0, 0

def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for i in range(4):
            if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=m or graph[x+dx[i]][y+dy[i]] == 0 or visited[x+dx[i]][y+dy[i]]:
                continue
            else:
                queue.append([x+dx[i], y+dy[i]])
                
t = int(sys.stdin.readline())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for j in range(k):
        str = list(map(int, sys.stdin.readline().strip().split()))
        graph[str[1]][str[0]] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)