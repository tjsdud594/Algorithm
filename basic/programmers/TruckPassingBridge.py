### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

###############################
#           풀이완료           #
###############################


def solution(bridge_length, weight, truck_weights):
    from collections import deque
    answer = 0

    on_bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    now_bridge = 0

    while truck_weights:
        answer+=1
        now_bridge -= on_bridge.popleft()
        if now_bridge+truck_weights[0]<=weight:
            now_bridge+=truck_weights[0]
            on_bridge.append(truck_weights.popleft())
        else:
            on_bridge.append(0)

    return answer+len(on_bridge)


if __name__ == "__main__":
    import time

    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]

    start = time.time()
    print(solution(bridge_length, weight, truck_weights))
    end = time.time()

    print(f"{end - start:.5f} sec")