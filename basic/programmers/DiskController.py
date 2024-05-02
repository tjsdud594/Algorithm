### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42627

###############################
#           풀이완료           #
###############################



def solution(jobs):
    import heapq
    import math

    answer = 0
    now = 0
    start = -1
    heap = []
    i = 0

    while i < len(jobs):
        for job in jobs:
            # 이전 job 종료시간과 현재 시간 사이에 요청된 job일 경우 대기열에 넣기
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                # print(heap)

        if heap:
            i+=1
            spent_time, start_time = heapq.heappop(heap)
            start = now
            # 각 job의 종료시간을 더하여 이전 job의 종료시간 체크
            now += spent_time
            # 해당 job의 대기+실행시간 누적
            answer+=(now-start_time)
        else:
            now+=1

        # print(f"start : {start}, now : {now}")

    return math.trunc(answer/len(jobs))


if __name__ == "__main__":
    import time

    jobs = [[0, 3], [1, 9], [2, 6]]

    start = time.time()
    print(solution(jobs))
    end = time.time()

    print(f"{end - start:.5f} sec")
