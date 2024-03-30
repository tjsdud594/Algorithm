### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43164

###############################
#           풀이중           #
###############################


def solution(tickets):
    from collections import defaultdict
    answer = []
    airport_dict = defaultdict(list)
    for airport in tickets:
        airport_dict[airport[0]].append(airport[1])

    # 각 공항 방문순서대로 정렬
    for airport in airport_dict.keys():
        airport_dict[airport]=sorted(airport_dict[airport])
    
    # print(airport_dict)

    def dfs(now):
        while airport_dict[now]:
            dfs(airport_dict[now].pop(0))
        answer.append(now)
        
    dfs('ICN')

    return answer[::-1]


if __name__ == "__main__":
    import time
    import random

    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    start = time.time()
    print(solution(tickets))
    end = time.time()

    print(f"{end - start:.5f} sec")