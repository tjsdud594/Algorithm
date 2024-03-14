### 문제 : https://www.acmicpc.net/problem/2178

###############################
#           풀이 완료          #
###############################

from collections import deque

maze = []
n, m = map(int, input().split())
for i in range(n):
    maze.append(list(map(int, list(input()))))

answer = []
q = deque([])
q.append([0,0])

# 아래 오른쪽 위 왼쪽 움직임
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    y, x = q.popleft()

    for my, mx in moves:
        if y+my<0 or x+mx<0 or y+my>=n or x+mx>=m:
            continue
        if (y+my)==n-1 and (x+mx)==m-1:
            answer.append(maze[y][x]+1)
            break
        if maze[y+my][x+mx]==1:
            q.append([y+my, x+mx])
            maze[y+my][x+mx]=maze[y][x]+1

print(min(answer))
