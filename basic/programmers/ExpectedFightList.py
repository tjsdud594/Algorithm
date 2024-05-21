### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12985

###############################
#           풀이 중          #
###############################

def solution(n,a,b):
    import math
    non_fight = 0
    max_cnt=int(math.log2(n))
    # print(max_cnt)
    big_num=max(a,b)
    small_num=min(a,b)
    # print(f"big: {big_num}, small: {small_num}")

    left=1
    right=n
    
    while 1:
        print(f"{left}~{right}   // {non_fight}")
        if left==small_num and right==big_num:
            break
        elif (right//2)>=big_num:
            print("왼쪽무리를 골라요")
            left=left
            right=right//2
            non_fight+=1
        elif (right//2)+1<=small_num:
            print("오른쪽무리를 골라요")
            left=(right//2)+1
            right=right
            non_fight+=1
        else:
            break
    # print(non_fight)
    return max_cnt-non_fight if max_cnt-non_fight>0 else max_cnt


if __name__ == "__main__":
    import time

    N=8
    A=4
    B=7

    start = time.time()
    print(solution(N, A, B))
    end = time.time()

    print(f"{end - start:.5f} sec")
