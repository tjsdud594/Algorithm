### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/62048

###############################
#           풀이완료           #
###############################

def solution(w, h):
    import math

    return (w*h) - (w + h - (math.gcd(w, h)))


if __name__ == "__main__":
    import time
    import random

    w = 8
    h = 12

    start = time.time()
    print(solution(w, h))
    end = time.time()

    print(f"{end - start:.5f} sec")