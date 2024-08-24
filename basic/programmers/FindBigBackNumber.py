### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/154539

###############################
#           풀이 완료          #
###############################

from heapq import *

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n):
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heappop(h)
            answer[idx] = value

        heappush(h, [value, i])
    return answer




if __name__ == "__main__":
    import time
    numbers = [2, 3, 3, 5]

    print("start")
    start = time.time()
    print(solution(numbers))
    end = time.time()

    print(f"{end - start:.5f} sec")
