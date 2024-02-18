### 문제 : https://www.acmicpc.net/problem/1260

###############################
#           풀이 완료          #
###############################


# 재귀함수 (종료조건을 확실하게 할 것!!)
# dfs 수정필요!!! deque로 앞에서부터 빼고 앞에서부터 넣는 방식으로!!
def dfs(start_node, nodes, graph, visited1):
    visited1[start_node]=True # 해당 노드 방문처리
    print(start_node, end=" ")
    for i in range(1, nodes+1):
        if not visited1[i] and graph[start_node][i]:
            dfs(i, nodes, graph, visited1)
    

def bfs(start_node, nodes, graph, visited2):
    q = deque([start_node])
    visited2[start_node]=True
    while q:
        visit_node=q.popleft()
        print(visit_node, end=" ")

        for i in range(1, nodes+1):
            if not visited2[i] and graph[visit_node][i]:
                q.append(i)
                visited2[i]=True


if __name__ == "__main__":
    import copy
    from collections import deque
    [nodes, lines, start_node] = list(map(int, input().split()))

    graph = [[False] * (nodes+1) for _ in range(nodes+1)]

    for _ in range(lines):
        a, b = map(int, input().split())
        graph[a][b]=True
        graph[b][a]=True        

    visited1=[False] * (nodes+1)  # 방문기록
    visited1[0]=True
    dfs(start_node, nodes, graph, visited1)
    print()

    visited2=[False] * (nodes+1)
    visited2[0]=True
    bfs(start_node, nodes, graph, visited2)



