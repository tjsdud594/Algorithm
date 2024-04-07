### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

###############################
#           풀이완료           #
###############################


def solution(tickets):
    from collections import defaultdict
    answer = []
    airport_dict = defaultdict(list)
    for start, end in tickets:
        airport_dict[start].append(end)

    for airport in airport_dict:
        airport_dict[airport] = sorted(airport_dict[airport])

    # 가장 마지막에 가는 공항부터 append
    def dfs(now):
        while airport_dict[now]:
            dfs(airport_dict[now].pop(0))
        answer.append(now)

    dfs("ICN")
    return answer[::-1]


if __name__ == "__main__":
    import time
    import random

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    start = time.time()
    print(solution(tickets))
    end = time.time()

    print(f"{end - start:.5f} sec")