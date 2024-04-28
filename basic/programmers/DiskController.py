### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42627

###############################
#           풀이완료           #
###############################


import heapq

def solution(jobs):
    answer = 0
    now = 0 #현재시간
    i = 0   #처리개수
    start = -1 #마지막 완료시간
    heap = []  # 
    
    while i < len(jobs):
        for job in jobs:
            # 요청시간이 이전 잡 완료시간과 현재 사이일때
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])  # 작업시간 기준으로 우선순위 부여하여 heap 생성, 작업이 짧을 수록 우선순위 상향, (작업시간, 요청시간)
                print(heap)
        
        if heap:
            current = heapq.heappop(heap)
            print(f"current : {current}")
            start = now
            now += current[0]
            answer += now - current[1] #요청으로부터 처리시간
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)


if __name__ == "__main__":
    import time

    jobs = [[0, 3], [1, 9], [2, 6]]

    start = time.time()
    print(solution(jobs))
    end = time.time()

    print(f"{end - start:.5f} sec")
