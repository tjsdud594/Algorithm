### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42860

###############################
#           풀이 완료          #
###############################

def solution(triangle):
    import copy
    answer =  copy.deepcopy(triangle)

    def sum_node(y, x):
        if y==0 and x==0:
            answer[y][x] = triangle[y][x]
        else:
            if x==0:
                answer[y][x] = answer[y][x]+answer[y-1][x]
            elif x==len(answer[y])-1:
                answer[y][x] = answer[y][x]+answer[y-1][x-1]
            else:
                answer[y][x] = max(answer[y][x]+answer[y-1][x], answer[y][x]+answer[y-1][x-1])

    for l in range(len(triangle)):
        for ll in range(len(triangle[l])):
            sum_node(l, ll)

    return max(answer[-1])

if __name__ == "__main__":
    import time
    import random

    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    start = time.time()
    print(solution(triangle))
    end = time.time()

    print(f"{end - start:.5f} sec")
