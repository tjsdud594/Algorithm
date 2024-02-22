### 문제 : https://www.acmicpc.net/problem/1260

###############################
#           풀이 완료          #
###############################


def dfs(visit, nodes, start):
    print(start, end=" ")

    if False not in visit.values():
        return
    
    for i in range(1, len(nodes)):
        if visit[i]==False and nodes[start][i]==True:
            visit[i]=True
            dfs(visit, nodes, i)

def bfs(visit, nodes, start):
    from collections import deque

    q = deque([start])

    while q:
        now = q.popleft()
        print(now, end=" ")

        for i in range(1, len(nodes)):
            # 아직 방문을 안했고 방문예정이라면
            if visit[i]==False and nodes[now][i]==True:
                q.append(i)
                visit[i]=True


if __name__ == "__main__":
    
    N, M, V = map(int, input().split(" "))
    
    visit_dfs = {x: False for x in range(1, N+1)}
    visit_bfs = {x: False for x in range(1, N+1)}
    nodes = [[False for _ in range(N+1)] for __ in range(N+1)]

    visit_dfs[V] = True
    visit_bfs[V] = True

    for _ in range(M):
        a, b = map(int, input().split(" "))
        nodes[a][b] = True
        nodes[b][a] = True

    dfs(visit_dfs, nodes, V)
    print()
    bfs(visit_bfs, nodes, V)
    



