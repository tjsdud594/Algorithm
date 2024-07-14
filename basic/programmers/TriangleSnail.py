### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

###############################
#           풀이완료           #
###############################


def solution(n):
    answer = []
    cnt = 1
    tri = []

    ## 삼각형 형태 리스트 생성
    while cnt <= n:
        tri.append([0 for _ in range(0, cnt)])
        cnt+=1

    x, y = 0, 0
    num = 1
    end_num = (n*(n+1))//2
    direction = [(1, 0), (0, 1), (-1, -1)]
    turn = 0

    while num<=end_num:
        
        tri[y][x] = num
        num+=1
        
        dy, dx = direction[turn]
        ny = y+dy
        nx = x+dx

        if 0<=ny<n and 0<=nx<n and tri[ny][nx] ==0:
            y, x = ny, nx
        else:
            turn = (turn + 1) % 3
            dy, dx = direction[turn]
            y+=dy
            x+=dx

    return [x for y in tri for x in y]


if __name__ == "__main__":
    import time

    n = 5

    start = time.time()
    print(solution(n))
    end = time.time()

    print(f"{end - start:.5f} sec")