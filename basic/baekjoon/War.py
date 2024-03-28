### 문제 : https://www.acmicpc.net/problem/1303

###############################
#           풀이 완료          #
###############################

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

group = []

for _ in range(M):
    group.append(list(sys.stdin.readline())[:-1])

# 상하좌우 이동
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
w_score = 0
b_score = 0

q = deque([])

def bfs(point, q, find_side):
    cnt=0
    q.append(point)
    while q:
        (y, x) = q.popleft()
        group[y][x]='X'

        cnt+=1
        for (mv_y, mv_x) in mv:
            if (y+mv_y)<0 or (y+mv_y)>=M or (x+mv_x)<0 or (x+mv_x)>=N:
                continue
            elif group[y+mv_y][x+mv_x]==find_side:
                q.append((y+mv_y, x+mv_x))
                group[y+mv_y][x+mv_x]='X'
    return cnt*cnt

for y in range(M):
    for x in range(N):
        if group[y][x]!='X':
            if group[y][x]=='W':
                w_score+=bfs((y, x), q, group[y][x])
            else:
                b_score+=bfs((y, x), q, group[y][x])

print(w_score, b_score)
