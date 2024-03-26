### 문제 : https://www.acmicpc.net/problem/11724

###############################
#           풀이 완료          #
###############################

## dfs 방법 
import sys
sys.setrecursionlimit(10000)  ## python에서 정해준 깊이 탐색 길이를 벗어나게 되면 오류가 발생하므로 탐색길이 재설정

group_cnt=0
N, M = map(int, sys.stdin.readline().split(' '))  ## sys로 입력을 받으면 시간초과 문제 해결됨!!
line_conn = {x:[] for x in range(N+1)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    line_conn[a].append(b)
    line_conn[b].append(a)

visited = {y: False for y in range(1,N+1)}

def dfs(node, visited, line_conn):
    visited[node]=True
    for i in line_conn[node]:
        if not visited[i]:
            dfs(i, visited, line_conn)

for a in range(1, N+1):
    if not visited[a]:
        dfs(a, visited, line_conn)
        group_cnt+=1

print(group_cnt)


