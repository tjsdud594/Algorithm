### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120875

###############################
#           풀이 완료          #
###############################

def solution(dots):
    com_list = [[(0,1), (2,3)], [(0,2), (1,3)], [(0,3), (1,2)]]

    for [a, b] in com_list: 
        print(a, b)
        # 첫번째 선분 기울기
        first = (dots[a[0]][0] - dots[a[1]][0])/(dots[a[0]][1] - dots[a[1]][1])

        # 두번째 선분 기울기
        second = (dots[b[0]][0] - dots[b[1]][0])/(dots[b[0]][1] - dots[b[1]][1])

        if first==second:
            return 1

    return 0



if __name__ == "__main__":
    import time
    dots = [[1,1], [4,2], [5,5], [7,7]]

    print("start")
    start = time.time()
    print(solution(dots))
    end = time.time()

    print(f"{end - start:.5f} sec")