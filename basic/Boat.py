### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

###############################
#           푸는중            #
###############################


# 생각을 잘못했음 최솟값끼리 더하는게 아니라 연속수합 구하듯이 최솟값+최댓값이 limit 아래로 오도록 조합을 짰어야한다.
def solution(people, limit):
    # answer = 0
    # 한 번에 최대 2명씩!!!
    # list sort
    sorted_people = sorted(people)
    print(sorted_people)    
    
    # 작은값부터 정하기(index while문)
    index = 0
    total_weight = 0
    boat_people_cnt = 0  
    while index<len(people):
        # index 0부터 시작해서 
        # 가장 index==0은 무게+1, people_cnt+1
        if index==0:
            answer=1  # 첫사람을 태울보트
            boat_people_cnt+=1  # 첫번째 사람이 탔다
            total_weight+=sorted_people[index]  # 첫번째 사람의 무게
            index+=1
            print(f"첫사람")
            print(f"answer : {answer}")
            print(f"boat_people_cnt : {boat_people_cnt}")
            print(f"total_weight : {total_weight}")
            print("===========================================================================")

        else:
            # 만약 지금 보트를 타려는 사람이 limit 절반을 넘는 무게를 가졌다면 이후의 사람들은 모두 보트1대씩 타게된다.
            if sorted_people[index]>(limit//2)+1 and (total_weight+sorted_people[index])>limit:
                answer+=(len(sorted_people)-index)
                print(f"limit 절반초과")
                print(f"answer : {answer}")
                print(f"boat_people_cnt : {boat_people_cnt}")
                print(f"total_weight : {total_weight}")
                print("===========================================================================")
                break

            else:

                total_weight+=sorted_people[index]

                # 무게를 초과했을경우 -> 새보트
                # 보트인원(2)을 초과했을경우 -> 새보트
                # 무게는 초과하지 않았지만 보트인원을 초과했을경우(3이상) -> 새보트
                print("현재 보트 상태")
                print(f"인원수 : {answer}")
                print(f"보트무게 : {total_weight}")
                print(f"탑승자수 : {boat_people_cnt}")
                print("===========================================================================")

                if (total_weight>limit) or (boat_people_cnt>2):
                    answer+=1 # 보트개수+1(현재사람이 탈 보트)
                    boat_people_cnt=1 # 인원수 초기화
                    total_weight=sorted_people[index] # 무게 조기화
                    # index+=1 # 다음사람으로 넘어감
                    print(f"초과해서 다음사람으로 넘어감")
                    print(f"answer : {answer}")
                    print(f"boat_people_cnt : {boat_people_cnt}")
                    print(f"total_weight : {total_weight}")
                    print("===========================================================================")

                else:
                    answer+=0
                    boat_people_cnt+=1
                    total_weight=total_weight
                    print(f"초과안해서 그대로 추가됨")
                    print(f"answer : {answer}")
                    print(f"boat_people_cnt : {boat_people_cnt}")
                    print(f"total_weight : {total_weight}")
                    print("===========================================================================")
            
            index+=1

            # 무게도 초과하지 않고 보트인원도 초과하지 않았을경우(0,1) -> 현재 보트에 인원 및 무게추가

        
    return answer


if __name__ == "__main__":
    import time

    start = time.time()
    people = [40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
    limit = 130
    # people = [41, 42, 43, 44]
    # limit = 200
    print(solution(people, limit))
    end = time.time()

    print(f"{end - start:.5f} sec")