### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/148653

###############################
#           풀이 완료          #
###############################

def solution(storey):
    answer = 0
    ## 큰수에서 중간값 이상일때는 빼는게 이득
    while storey:
        remain = storey%10
        # 6,7,8,9
        if remain>5:
            answer += (10-remain)
            storey += 10
        #0,1,2,3,4
        elif remain<5:
            answer += remain
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remain
        storey //= 10

    return answer


if __name__ == "__main__":
    import time

    storey=88

    start = time.time()
    print(solution(storey))
    end = time.time()

    print(f"{end - start:.5f} sec")
