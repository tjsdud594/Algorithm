### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

###############################
#           풀이완료           #
###############################


def solution(n):

    num = 1
    max_num = (n*(n+1))//2
    turn = 0
    turn_list = [(1, 0), (0, 1), (-1, -1)]  # 아래, 오른쪽, 위
    x, y = 0, 0
    triangle = []

    ## 토대 리스트 생성
    for i in range(1, n+1):
        triangle.append([0 for _ in range(i)])

    while num<=max_num:
        triangle[y][x] = num
        num+=1
        my, mx = turn_list[turn]
        ny = y+my
        nx = x+mx

        if 0<=ny<n and 0<=nx<n and triangle[ny][nx]==0:
            y = ny
            x = nx
            
        else:
            turn = (turn + 1) % 3
            my, mx = turn_list[turn]
            y+=my
            x+=mx

    return [b for a in triangle for b in a]


if __name__ == "__main__":
    import time

    n = 6

    start = time.time()
    print(solution(n))
    end = time.time()

    print(f"{end - start:.5f} sec")