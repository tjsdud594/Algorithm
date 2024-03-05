### 문제 : https://www.acmicpc.net/problem/2667

###############################
#           풀이 완료          #
###############################

from collections import deque

answer_list=[]

# 방문한 곳을 0으로 바꾸고 지나가도록 설정!!
def find_group(groups, start:deque):

    global cnt

    mv_list = [(1,0), (-1,0), (0,1), (0,-1)]

    while start:
        y, x = start.popleft()
        cnt+=1

        for my, mx in mv_list:
            if y+my>len(groups)-1 or y+my<0 or x+mx>len(groups[0])-1 or x+mx<0:
                continue

            else:
                if groups[y+my][x+mx]=='1':
                    start.append((y+my, x+mx))
                    groups[y+my][x+mx]='0'  # 방문한 위치
                else:
                    continue

    return cnt

def find_one(groups):

    start = deque([])

    global cnt, answer_list
    cnt=0

    start_y, start_x = 0, 0

    for y in range(0, len(groups)):
        for x in range(0, len(groups[0])):
            if groups[y][x]=='1':
                start_y=y
                start_x=x
                groups[y][x]='0'
                start.append((start_y, start_x))
                find_group(groups, start)
                answer_list.append(cnt)
                cnt=0
            
            else:
                continue

    return answer_list

groups = []

line_num = int(input())
for _ in range(line_num):
    groups.append(list(input()))

find_one(groups)

answer_list = sorted(answer_list)

print(len(answer_list))
for a in answer_list:
    print(a)