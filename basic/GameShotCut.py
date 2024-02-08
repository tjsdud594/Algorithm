### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

###############################
#           풀이 완료          #
###############################

from collections import deque

def solution(maps):
    queue = deque()

    # 상하좌우 이동
    move_x = [0, 0, -1, 1]
    move_y = [-1, 1, 0, 0]

    y, x = 0, 0
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + move_y[i]
            nx = x + move_x[i]

            # 범위 초과하면 무시
            if nx<0 or ny<0 or nx>=len(maps[0]) or ny>=len(maps):
                continue

            # 벽이면 무시
            if maps[ny][nx]==0:
                continue

            # 처음 지나가는 길이면 거리계산 후 다시 상하좌우 확인
            if maps[ny][nx]==1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    return maps[len(maps)-1][len(maps[0])-1] if maps[len(maps)-1][len(maps[0])-1]!=1 else -1



if __name__ == "__main__":
    import time
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

    print("start")
    start = time.time()
    print(solution(maps))
    # solution(maps)
    end = time.time()

    print(f"{end - start:.5f} sec")
