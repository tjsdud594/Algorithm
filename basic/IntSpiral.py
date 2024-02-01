### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/181832

###############################
#           풀이 완료          #
###############################

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    y=0
    x=0
    direction = "right"  # right, down, left, top, right

    for i in range(1, n*n+1):

        answer[y][x] = i

        if direction=="right":
            if x+1==n or answer[y][x+1]!=0:
                direction="down"
                y+=1
            else:
                x+=1

        elif direction=="down":
            if y+1==n or answer[y+1][x]!=0:
                direction="left"
                x-=1
            else:
                y+=1

        elif direction=="left":
            if answer[y][x-1]!=0:
                direction="top"
                y-=1
            else:
                x-=1

        elif direction=="top":
            if answer[y-1][x]!=0:
                direction="right"
                x+=1
            else:
                y-=1


    return answer


if __name__ == "__main__":
    import time
    n = 4

    print("start")
    start = time.time()
    print(solution(n))
    end = time.time()

    print(f"{end - start:.5f} sec")


