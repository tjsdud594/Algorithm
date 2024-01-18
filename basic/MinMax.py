### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12939

###############################
#           풀이완료           #
###############################

def solution(s):
    lst = [int(i) for i in s.split()]
    return f"{min(lst)} {max(lst)}"

if __name__ == "__main__":
    import time
    import random

    lst = [str(random.randint(-100000000, 100000000)) for _ in range(1000000)]  # 100 만건
    
    s = " ".join(lst)

    start = time.time()
    print(solution(s))
    end = time.time()

    print(f"{end - start:.5f} sec")


