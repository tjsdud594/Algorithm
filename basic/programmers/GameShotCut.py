### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

###############################
#           오답 완료          #
###############################

from collections import deque

# 최단거리, 최선의 경우를 구할때는 bfs를 주로 사용한다.
def solution(maps):
    load_list=deque()

    y, x = 0, 0
    load_list.append((y, x))
    len_y = len(maps)
    len_x = len(maps[0])

    while load_list:
        (y, x) = load_list.popleft()
        # 적진에 도달하면 멈춘다.
        if y==len_y-1 and x==len_x-1:
            return maps[y][x]
        
        # 상하좌우 이동
        # 상 y-1, x / 하 y+1, x / 좌 y, x-1 / 우 y, x+1
        move=[(-1, 0), (1, 0), (0, -1), (0, 1)]

        for (ym, xm) in move:
            # 범위를 초과하면 pass
            if y+ym<0 or y+ym>len_y-1 or x+xm<0 or x+xm>len_x-1:
                continue
            # 벽이면 pass
            elif maps[y+ym][x+xm]==0:
                continue
            else:
                if maps[y+ym][x+xm]==1:
                    maps[y+ym][x+xm] = maps[y][x]+1
                    load_list.append((y+ym, x+xm))

    return -1




if __name__ == "__main__":
    import time
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

    print("start")
    start = time.time()
    print(solution(maps))
    # solution(maps)
    end = time.time()

    print(f"{end - start:.5f} sec")
