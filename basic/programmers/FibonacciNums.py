### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12945

###############################
#           풀이완료           #
###############################

def solution(n):
    fibo_dict = {0:0, 1:1}
    key=1
    while key<n:
        key+=1
        fibo_dict[key] = fibo_dict[key-1] + fibo_dict[key-2]
    return fibo_dict[n]%1234567


if __name__ == "__main__":
    import time

    n = 10

    start = time.time()
    print(solution(n))
    end = time.time()

    print(f"{end - start:.5f} sec")