### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/152996

###############################
#           풀이 완료          #
###############################

from collections import Counter

def solution(weights):
    answer = 0
    w_cnt = Counter(weights)

    ## 같은 무게인 사람 체크
    for k in w_cnt.keys():
        if w_cnt[k]>1:
            answer += (w_cnt[k]*(w_cnt[k]-1))//2

    ## 각 짝꿍 찾기
    ratio_list = [(2,3), (1,2), (3,4)]
    for w in w_cnt.keys():
        for u,d in ratio_list:
            if w_cnt[(w*u)/d]:
                answer+=(w_cnt[int((w*u)/d)])*w_cnt[w]

    return answer

if __name__ == "__main__":
    import time

    weights=[100,180,360,100,270,100]

    start = time.time()
    print(solution(weights))
    end = time.time()

    print(f"{end - start:.5f} sec")

