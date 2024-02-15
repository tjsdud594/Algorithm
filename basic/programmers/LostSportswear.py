### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

###############################
#           풀이 완료          #
###############################


def solution(n, lost, reserve):
    af_lost = sorted(list(set(lost)-set(reserve)))
    af_reserve = sorted(list(set(reserve)-set(lost)))

    answer=n-len(af_lost)
    
    for num in af_lost:
        front_num = num-1
        back_num = num+1
        if (front_num) in af_reserve:
            af_reserve.remove(front_num)
            answer+=1
        elif (back_num) in af_reserve:
            af_reserve.remove(back_num)
            answer+=1

    return answer


if __name__ == "__main__":
    import time
    n = 10
    lost = [1,3,4,6]
    reserve = [1,3,5,8]

    print("start")
    start = time.time()
    print(solution(n, lost, reserve))
    end = time.time()

    print(f"{end - start:.5f} sec")