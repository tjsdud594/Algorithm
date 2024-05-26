### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12914

###############################
#           풀이 완료          #
###############################

def solution(n):
    from math import factorial
    answer = 0
    max_two = int(n//2)
    for two_cnt in range(max_two+1):
        one_cnt = n-(2*two_cnt)
        # print(tmp_list)
        # print(set(permutations(tmp_list, one_cnt+two_cnt)))
        # print(f"one : {one_cnt}, two : {two_cnt}")
        answer+=factorial(two_cnt+one_cnt)//(factorial(one_cnt)*factorial(two_cnt))
        # print(answer)
    return answer%1234567


if __name__ == "__main__":
    import time

    N=2000

    start = time.time()
    print(solution(N))
    end = time.time()

    print(f"{end - start:.5f} sec")
