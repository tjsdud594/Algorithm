### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12900

###############################
#           풀이중           #
###############################

## 재귀는 시간초과 걸림

import sys
sys.setrecursionlimit(10**7)

## 시간초과
# def solution(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
    
#     return (solution(n-1)+solution(n-2))%1000000007

# 1000000007 초과할 때만 나머지계산
def solution(n):
    answer = [0 for _ in range(n)]
    answer[0] = 1
    answer[1] = 2

    for i in range(2, n):
        sum = answer[i-1] + answer[i-2]
        if sum>1000000007:
            answer[i] = sum%1000000007
        else:
            answer[i] = sum

    return answer[-1]


if __name__ == "__main__":
    import time

    n = 4
    start = time.time()
    print(solution(n))
    end = time.time()

    print(f"{end - start:.5f} sec")