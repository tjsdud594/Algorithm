### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/154539

###############################
#           풀이 완료          #
###############################

from heapq import *

def solution(numbers):
    answer = [-1] * len(numbers)
    heap = []

    for i in range(len(numbers)):
        value = numbers[i]

        ## heap의 최솟값이 value보다 작으면 answer에 기재 
        while heap and heap[0][0] < value:
            _, idx = heappop(heap)
            answer[idx] = value

        heappush(heap, [value, i])

    return answer



if __name__ == "__main__":
    import time
    numbers = [2, 3, 3, 5]

    print("start")
    start = time.time()
    print(solution(numbers))
    end = time.time()

    print(f"{end - start:.5f} sec")
