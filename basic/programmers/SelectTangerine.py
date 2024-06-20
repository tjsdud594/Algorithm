### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/138476

###############################
#           풀이중           #
###############################

def solution(k, tangerine):
    from collections import Counter
    answer = 0
    in_bucket = 0

    cnt_per_size = Counter(tangerine)
    cnt_list = sorted(cnt_per_size.values(), reverse=True)
    print(cnt_per_size)
    print(cnt_list)

    for cnt in cnt_list:
        answer+=1
        in_bucket+=cnt
        if in_bucket>=k:
            break

    return answer


if __name__ == "__main__":
    import time

    k = 6
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

    start = time.time()
    print(solution(k, tangerine))
    end = time.time()

    print(f"{end - start:.5f} sec")