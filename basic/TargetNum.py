### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

###############################
#           풀이 완료          #
###############################

## BFS : 최선의 경우를 구할때 주로 사용한다!
def solution_bfs(numbers, target):

    super_node = [0]

    for num in numbers:
        temp = []

        for node in super_node:
            temp.append(node+num)
            temp.append(node-num)

        super_node=temp

    return super_node.count(target)

## DFS : 주로 재귀함수로 구현한다!
def dfs(numbers, target, idx, values):
    # print(values)

    global cnt 
    # cnt = 0


    if idx!=len(numbers):
        dfs(numbers, target, idx+1, values + numbers[idx])
        dfs(numbers, target, idx+1, values - numbers[idx])

    else:
        if values==target:
            cnt+=1
        return

def solution_dfs(numbers, target):

    global cnt
    cnt=0
    dfs(numbers, target, 0, 0)


    return cnt

if __name__ == "__main__":
    import time
    numbers = [4, 1, 2, 1]
    target=4

    print("start")
    start = time.time()
    print(solution_dfs(numbers, target))
    end = time.time()

    print(f"{end - start:.5f} sec")

