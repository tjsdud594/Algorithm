### 문제 : https://www.acmicpc.net/problem/2606

###############################
#           풀이 완료          #
###############################

def virus(visited, node_connect, start_node):
    global cnt
    
    for i in range(len(node_connect)):
        if visited[i]==False and node_connect[i][start_node]==True:
            visited[i]=True
            cnt+=1
            # print(visited, cnt)
            virus(visited, node_connect, i)
    return cnt

c_num = int(input())

node_connect = [[False for _ in range(c_num+1)] for __ in range(c_num+1)]
visited = {x:False for x in range(c_num+1)}
visited[0]=True
visited[1]=True

line_num = int(input())

for _ in range(line_num):
    a,b = map(int, input().split(" "))
    node_connect[a][b] = True
    node_connect[b][a] = True
#     # print("**", a,b ,"**")

# for ll in node_connect:
#     print(ll)

cnt=0

print(virus(visited, node_connect, 1))
