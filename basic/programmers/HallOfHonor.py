### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

###############################
#           풀이완료           #
###############################

import heapq

def solution(k, score):
    answer = []
    sc_cut = []
    min_sc = float('inf')

    for sc in score:
        if len(sc_cut)<k:
            heapq.heappush(sc_cut, sc)
            min_sc = min(min_sc, sc)

        else:
            if sc > min_sc:
                heapq.heappop(sc_cut)
                heapq.heappush(sc_cut, sc)
                min_sc = heapq.heappop(sc_cut)
                heapq.heappush(sc_cut, min_sc)
        answer.append(min_sc)

    return answer
    

if __name__ == "__main__":
    import time

    k  = 3
    score = [10, 100, 20, 150, 1, 100, 200]

    start = time.time()
    print(solution(k, score))
    end = time.time()

    print(f"{end - start:.5f} sec")