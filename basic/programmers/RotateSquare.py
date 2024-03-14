# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/77485

###############################
#           풀이 완료          #
###############################

def solution(rows, columns, queries):
    from collections import deque
    import copy

    num_pad = [[0 for _ in range(0, rows)] for __ in range(0, columns)]

    num = 1
    for i in range(0, rows):
        for j in range(0, columns):
            num_pad[i][j] = num
            num+=1

    queries=deque(queries)
    answer = []
    ans = float('inf')

    while queries:
        [start_y, start_x, end_y, end_x] = queries.popleft()
        start_x-=1
        start_y-=1
        end_x-=1
        end_y-=1
        y=copy.deepcopy(start_y)
        x=copy.deepcopy(start_x)
        bf_num=num_pad[y][x]

        nums = deque([])
        nums.append(num_pad[y][x])

        for _ in range(((end_x-start_x+1)*2)+((end_y-start_y+1)*2)-4):
            print(f"(y,x) : ({y}, {x}) = {num_pad[y][x]}")
            replace_num = nums[-1]
        
            # 오른쪽으로 이동
            if y==start_y and start_x<=x and x<end_x:
                bf_num=num_pad[y][x+1]
                num_pad[y][x+1] = replace_num
                nums.append(bf_num)
                x+=1

                continue

            # 아래로 이동
            elif x==end_x and start_y<=y and y<end_y:
                bf_num=num_pad[y+1][x]
                num_pad[y+1][x] = replace_num
                nums.append(bf_num)
                y+=1

                continue

            # 왼쪽으로 이동
            elif y==end_y and start_x<x and x<=end_x:
                bf_num=num_pad[y][x-1]
                num_pad[y][x-1] = replace_num
                nums.append(bf_num)
                x-=1

                continue

            # 위로 이동
            elif x==start_x and start_y<y and y<=end_y:
                bf_num=num_pad[y-1][x]
                num_pad[y-1][x] = replace_num
                nums.append(bf_num)
                y-=1

                continue

        for i in num_pad:
            print(i)
        answer.append(min(nums))
        print(nums)
        print("=="*20)

    return answer


if __name__ == "__main__":
    import time
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

    print("start")
    start = time.time()
    print(solution(rows, columns, queries))
    end = time.time()

    print(f"{end - start:.5f} sec")
