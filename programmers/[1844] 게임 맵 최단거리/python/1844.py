from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]
    dis = [[0] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    dis[0][0] = 1
        
    while queue:
        now = queue.popleft()
            
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
                
            if 0<=x<=n-1 and 0<=y<=m-1:
                if maps[x][y] == 1 and visited[x][y] == 0:
                    visited[x][y] = 1
                    dis[x][y] = dis[now[0]][now[1]] + 1
                    queue.append((x, y))
    
    result = -1 if dis[n-1][m-1] == 0 else dis[n-1][m-1]
    return result
            
        
            
        
        
        