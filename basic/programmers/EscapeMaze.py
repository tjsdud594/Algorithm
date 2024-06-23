### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/159993

###############################
#           풀이중           #
###############################

from collections import deque

def bfs(map, x, y, goal):
    
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0 for _ in range(len(map[0]))] for __ in range(len(map))]

    q = deque([])
    q.append((y,x))

    while q:
        y, x = q.popleft()

        if map[y][x] == goal:
            for a in visited:
                print(a)
            return visited[y][x]

        for (move_y, move_x) in move:

            if 0<=y+move_y<len(map) and 0<=x+move_x<len(map[0]) and map[y+move_y][x+move_x]!="X" and visited[y+move_y][x+move_x]==0:
                visited[y+move_y][x+move_x]=visited[y][x]+1
                q.append((y+move_y, x+move_x))
    return -1


def solution(maps):

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sy, sx = i, j

            elif maps[i][j] == "L":
                ly, lx = i, j

    ## 레버찾기
    find_lever = bfs(maps, sx, sy, "L")
    print(find_lever)

    ## 출구찾기
    find_exit = bfs(maps, lx, ly, "E")
    print(find_exit)

    if find_lever==-1 or find_exit==-1:
        return -1

    return find_lever + find_exit




if __name__ == "__main__":
    import time

    maps = ["XXXXL", "XOOSX", "XXXXX", "XXXOO", "EXXXX", "XXXXX"]

    start = time.time()
    print(solution(maps))
    end = time.time()

    print(f"{end - start:.5f} sec")