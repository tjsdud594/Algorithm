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


def solution2(operations):
    import heapq
    answer = []

    for instance in operations:
        op, val = instance.split()
        heapq.heapify(answer)

        if op=="I":
            heapq.heappush(answer, int(val))
        else:
            if answer==[]:
                continue
            elif val=="-1":
                heapq.heappop(answer)
            else:
                heapq._heapify_max(answer)
                heapq.heappop(answer)
        # print(f"instance : {instance}, answer : {answer}")

    min_heap = answer[:]
    heapq.heapify(min_heap)
    max_heap = answer[:]
    heapq._heapify_max(max_heap)
    return [max_heap[0], min_heap[0]] if answer!=[] else [0,0]


if __name__ == "__main__":
    import time

    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

    start = time.time()
    print(solution2(operations))
    end = time.time()

    print(f"{end - start:.5f} sec")

