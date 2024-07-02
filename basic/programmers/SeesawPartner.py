### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/152996

###############################
#           풀이 완료          #
###############################

from collections import Counter

def solution(weights):
    answer = 0
    new_weights = list(set(weights))
    w_cnt = Counter(weights)

    ## 1:1
    for w in w_cnt.keys():
        if w_cnt[w]>1:
            answer+=(w_cnt[w]*(w_cnt[w]-1))//2

    check = (3/4, 1/2, 2/3)
    for w in new_weights:
        for c in check:
            answer+=w_cnt[w]*w_cnt[w*c]

    return answer

if __name__ == "__main__":
    import time

    weights=[100,180,360,100,270,100]

    start = time.time()
    print(solution(weights))
    end = time.time()

    print(f"{end - start:.5f} sec")

