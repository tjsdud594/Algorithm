### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/159993

###############################
#           풀이중           #
###############################

import collections 

def bfs(start_x, start_y, target_x, target_y, MAP):
    move = {(-1,0),(0,1),(1,0),(0,-1)}
    
    q = collections.deque()
    q.append((start_x, start_y, 0)) # cnt : 0
    
    visited = [[0 for _ in range(len(MAP[0]))] for _ in range(len(MAP))]
    visited[start_x][start_y] = 1
    
    while q:
        x, y, cnt = q.popleft()
        if x == target_x and y == target_y:
            return cnt
        
        for tx, ty in move:
            nx = tx + x
            ny = ty + y
            
            if 0<=nx<len(MAP) and 0<=ny<len(MAP[0]) and MAP[nx][ny] != 'X' and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                q.append((nx,ny,cnt+1))
                
    return -1
    

def solution(maps):
    total = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                sx, sy = i,j
            if maps[i][j] == 'L':
                lx, ly = i,j
            if maps[i][j] == 'E':
                ex, ey = i,j
            

    # 레버찾고
    before = bfs(sx, sy, lx, ly, maps)
    # 출구 찾기
    after = bfs(lx, ly, ex, ey, maps)
    
    if before == -1 or after == -1: 
        return -1
    
    return after + before

if __name__ == "__main__":
    import time

    maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

    start = time.time()
    print(solution(maps))
    end = time.time()

    print(f"{end - start:.5f} sec")