### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42898

###############################
#           풀이 완료          #
###############################

def solution(m, n, puddles):
    loads = [[1 for _ in range(m)] for __ in range(n)] 

    if puddles!=[[]]:
        for [x,y] in puddles:
            loads[y-1][x-1]=0

    x_num=1
    y_num=1
    for i in range(m):
        if loads[0][i]==0:
            x_num=0
        loads[0][i]=x_num
    for j in range(n):
        if loads[j][0]==0:
            y_num=0
        loads[j][0]=y_num
    
    for x in range(1, m):
        for y in range(1, n):
            if loads[y][x]==0:
                continue
            else:
                loads[y][x] = loads[y-1][x] + loads[y][x-1]

    return loads[n-1][m-1]%1000000007

if __name__ == "__main__":
    import time

    m=100
    n=100
    puddles=[]

    start = time.time()
    print(solution(m, n, puddles))
    end = time.time()

    print(f"{end - start:.5f} sec")

