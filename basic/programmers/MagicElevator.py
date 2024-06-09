### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/148653

###############################
#           풀이 완료          #
###############################

def solution(storey):
    answer = 0

    while storey:
        # 1의 자리수로 버튼 판단
        floor = storey%10
        ## 0~4 일경우 아래서부터 올라감
        if floor<5:
            answer+=floor
        ## 6~9 일경우 위에서부터 내려옴, 한자리 윗 수(10의 자리)에 +1
        elif floor>5:
            answer+=(10-floor)
            storey+=10
        ## 5일경우 해당 윗자리수를 보고 판단
        else:
            if (storey//10)%10 > 4:
                storey+=10
            answer+=floor
        storey//=10
        print(f"floor : {floor}, storey : {storey}, answer : {answer}")
    return answer


if __name__ == "__main__":
    import time

    storey=555

    start = time.time()
    print(solution(storey))
    end = time.time()

    print(f"{end - start:.5f} sec")
