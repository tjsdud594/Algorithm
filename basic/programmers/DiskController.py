### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42627

###############################
#           풀이완료           #
###############################



def solution(jobs):
    import heapq

    # 이전 잡이 끝난시간
    start = -1
    # 현재 잡이 끝날 시간
    now = 0
    # job 대기열
    heap = [] 
    # 완료한 job의 개수
    clear_job = 0
    answer = 0
    
    while clear_job<len(jobs):
        # print(f"heap : {heap}, start : {start}, now : {now}")
        for job_request, job_time in jobs:
            # 현재 잡이 실행 중일 때 대기열에 들어갈 경우 heap에 넣는다
            if start<job_request<=now:
                heapq.heappush(heap, [job_time, job_request])
            # print(f"heap : {heap}, start : {start}, now : {now}")
        
        # heap에 대기중인 잡들을 실행시간이 적은 순으로 실행
        if heap:
            t, req = heapq.heappop(heap)
            start = now
            now += t
            answer+= (now-req)
            clear_job+=1
            # print(f"heap : {heap}, start : {start}, now : {now}")

        else:
            now+=1
            # print(f"heap : {heap}, start : {start}, now : {now}")

    return answer//len(jobs)


if __name__ == "__main__":
    import time

    jobs = [[0, 3], [1, 9], [2, 6]]

    start = time.time()
    print(solution(jobs))
    end = time.time()

    print(f"{end - start:.5f} sec")
