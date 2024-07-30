# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

###############################
#           풀이 완료          #
###############################

def solution(queue1, queue2):
    from collections import deque
    answer = 0
    queue1 = deque(queue1)
    que1_sum = sum(queue1)
    queue2 = deque(queue2)
    que2_sum = sum(queue2)
    max_ans = len(queue1)*3

    while answer<=max_ans and que1_sum!=que2_sum:
        if que1_sum > que2_sum:
            num = queue1.popleft()
            que1_sum-=num
            que2_sum+=num
            queue2.append(num)
        else:
            num = queue2.popleft()
            que2_sum-=num
            que1_sum+=num
            queue1.append(num)

        answer+=1

    return answer if answer <= max_ans else -1

if __name__ == "__main__":
    import time
    queue1 = [1, 1, 1, 1]
    queue2 = [1, 1, 7, 1]

    print("start")
    start = time.time()
    print(solution(queue1, queue2))
    end = time.time()

    print(f"{end - start:.5f} sec")
