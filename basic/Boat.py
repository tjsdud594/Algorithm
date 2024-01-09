### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

###############################
#           푸는중            #
###############################
def solution(people, limit):
    # answer = 0
    # 한 번에 최대 2명씩!!!
    # list sort
    sorted_people = sorted(people)
    print(sorted_people)    
    
    # 작은값부터 정하기(index while문)
    index = 0
    total_weight = 0
    while index<len(people):
        # 가장 첫사람 추가
        if index==0:
            index=1
            total_weight = sorted_people[0]
            answer=1
            
        else:
            total_weight+=sorted_people[index]
            # 다음값을 더해서 한도초과 되지 않으면 index+=1 / answer그대로 / 무게는 다음사람껄로 대체
            # 사람 수 count가 필요하지 않을까? 2명까지만 탈수있으니까!
            if (total_weight)<=limit:
                total_weight = sorted_people[index]
                index+=1
                print("한도초과X")
                print(f"index : {index}")
                print(f"total_weight : {total_weight}")
                print(f"answer : {answer}")
                total_weight+=limit  # 최대값 더해서 강제로 다음으로 넘기기
            
            # 다음값을 더해서 한도초과 되면 index그대로 / answer+=1
            # 전체 스캔하지 말고 값이 limit/2 보다 크면 보트 개수 다 더하기
            else:
                answer+=1
                if sorted_people[index] > limit/2:
                    answer+=len(sorted_people)-(index)
                    break
                else:
                    total_weight=sorted_people[index]
                    index+=1
                    print("한도초과O")
                    print(f"index : {index}")
                    print(f"total_weight : {total_weight}")
                    print(f"answer : {answer}")
    # 마지막에 +1 하는것 때문에 오답이 많아지는듯 함
    return answer


if __name__ == "__main__":
    import time

    start = time.time()
    people = [70, 50, 80, 50]
    limit = 100
    # people = [41, 42, 43, 44]
    # limit = 200
    print(solution(people, limit))
    end = time.time()

    print(f"{end - start:.5f} sec")