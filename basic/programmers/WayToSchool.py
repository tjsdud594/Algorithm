### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

###############################
#           풀이 완료          #
###############################

def solution(m, n, puddles):

    map = [[1 for _ in range(m)] for __ in range(n)]
    if puddles!=[]:
        for puddle in puddles:
            [x, y] = puddle
            map[y-1][x-1]=0

    flag=1
    for x in range(m):
        if map[0][x]==0:
            flag=0
        map[0][x] = flag

    flag=1
    for y in range(n):
        if map[y][0]==0:
            flag=0
        map[y][0]=flag

    for y in range(1, n):
        for x in range(1, m):
            if map[y][x]!=0:
                map[y][x] = map[y-1][x] + map[y][x-1]

    return map[n-1][m-1]%1000000007

if __name__ == "__main__":
    import time

    m=7
    n=4
    puddles=[[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]

    start = time.time()
    print(solution(m, n, puddles))
    end = time.time()

    print(f"{end - start:.5f} sec")

