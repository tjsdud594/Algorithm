### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

###############################
#           푸는중            #
###############################
import time

# 생각을 잘못했음 최솟값끼리 더하는게 아니라 연속수합 구하듯이 최솟값+최댓값이 limit 아래로 오도록 조합을 짰어야한다.
def solution(people, limit):
    answer = 0
    total_people = len(people)

    # 사람이 2명 이하일 때
    if total_people<=2:
        if sum(people)>limit:
            return total_people
        else:
            return 1
    
    # 사람이 3명 이상일 때
    else:
        start = time.time()
        sorted_people = sorted(people)
        end = time.time()
        print(f"sort시간 : {end - start:.5f} sec")

        # print(sorted_people)
        least_weight = sorted_people[0]
        max_index=0

        start = time.time()
        for i in range(total_people-1, 0, -1):
            if least_weight+sorted_people[i]<=limit:
                max_index=i
                break
        end = time.time()
        print(f"같이 탈 수 있는 최저무게 찾기 : {end - start:.5f} sec")

        if max_index==0:
            return total_people
        
        else:
            answer+=(total_people-max_index)-1
            # print(f"초기 1인 탑승 : {answer}명")
            start_index=0
            start = time.time()
            while start_index<=max_index:
                if sorted_people[start_index]+sorted_people[max_index]>limit:
                    # print(f"무게초과 {sorted_people[start_index]}+{sorted_people[max_index]}")
                    max_index-=1
                    answer+=1
                    continue
                else:
                    # print(f"무게미달 {sorted_people[start_index]}+{sorted_people[max_index]}")
                    start_index+=1
                    max_index-=1
                    answer+=1
                    continue
            end = time.time()
            print(f"동반탑승 구분하기 : {end - start:.5f} sec")
        
    return answer


if __name__ == "__main__":
    import time
    import random

    start = time.time()
    # people = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    # limit = 100
    # people = [41, 42, 43, 44]
    # limit = 200
    people = [random.randint(40, 240) for _ in range(50000)]
    limit=240
    print(solution(people, limit))
    end = time.time()

    print(f"{end - start:.5f} sec")