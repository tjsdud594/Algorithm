### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43162

###############################
#           풀이 완료          #
###############################

# dfs로 풀어야 할듯?
# dfs로 가지 하나 타고 내려가다가 dfs 끝나고 방문 체크하고 방문 안한 노드 있으면 거기부터 다시 dfs 시작!!!

def solution(n, computers):
    from collections import deque
    global answer
    answer = 1

    # 방문한 노드 체크
    visited = [False] * (n)
    visited[0] = True

    def dfs(n, computers, start_node):
        global answer

        q = deque([start_node])

        while q:
            node = q.popleft()
            for i in range(n):
                if i==node:
                    continue
                if not visited[i] and (computers[node][i]):
                    q.append(i)
                    visited[i]=True
                    continue

        if False in visited:
            for idx, bool in enumerate(visited):
                if bool==False:
                    answer+=1
                    visited[idx]=True
                    dfs(n, computers, idx)
                    return answer
        else:
            return answer

    final_ans = dfs(n, computers, 0)

    return final_ans




if __name__ == "__main__":
    import time

    n = 3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    print("start")
    start = time.time()
    solution(n, computers)
    end = time.time()
    print("end")

    print(f"{end - start:.5f} sec")