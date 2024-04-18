### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42628

###############################
#           풀이완료           #
###############################


def solution(operations):
    from collections import deque
    answer = deque([])

    for instance in operations:
        transaction, code = instance.split()
        if transaction=="I":
            answer.append(int(code))
            answer = deque(sorted(answer, reverse=True))
        else:
            if answer==deque([]):
                continue
            elif code=="1":
                answer.popleft()
            else:
                answer.pop()
        # print(f"instance : {instance}, answer : {answer}")


    return [answer[0], answer[-1]] if answer!=deque([]) else [0, 0]



if __name__ == "__main__":
    import time

    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

    start = time.time()
    print(solution(operations))
    end = time.time()

    print(f"{end - start:.5f} sec")

