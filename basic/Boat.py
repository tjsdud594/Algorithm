### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

###############################
#           푸는중            #
###############################
def solution(people, limit):
    # answer = 0
    
    # list sort
    sorted_people = sorted(people)
    print(sorted_people)    
    
    # 작은값부터 정하기(index while문)
    index = 0
    total_weight = 0
    while index<=len(people)-2:
        if index==0:
            total_weight = sorted_people[index]
            answer=1
            index+=1
            
        else:
            total_weight+=sorted_people[index]
            # 다음값을 더해서 한도초과 되지 않으면 index+=1 / answer그대로
            if (total_weight)<=limit:
                index+=1
                print("한도초과X")
                print(f"index : {index}")
                print(f"total_weight : {total_weight}")
                print(f"answer : {answer}")
            
            # 다음값을 더해서 한도초과 되면 index그대로 / answer+=1
            # 전체 스캔하지 말고 값이 limit/2 보다 크면 보트 개수 다 더하기
            else:
                if sorted_people[index] > limit/2:
                    answer+=len(sorted_people)-(index)-1
                    break
                else:
                    answer+=1
                    total_weight=sorted_people[index]
                    index+=1
                    print("한도초과O")
                    print(f"index : {index}")
                    print(f"total_weight : {total_weight}")
                    print(f"answer : {answer}")
    return answer+1


if __name__ == "__main__":
    import time

    start = time.time()
    people = [45, 72, 89, 53, 65, 98, 40, 77, 54, 91, 79, 47, 60, 88, 94, 41, 68, 55, 83, 74]
    limit = 100
    print(solution(people, limit))
    end = time.time()

    print(f"{end - start:.5f} sec")