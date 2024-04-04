### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

###############################
#           풀이완료           #
###############################


def solution(bridge_length, weight, truck_weights):
    from collections import deque, defaultdict
    answer=0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0]*bridge_length)

    now_weight = 0
    while truck_weights:
        answer+=1
        now_weight-=on_bridge.popleft()

        # if sum(on_bridge)+truck_weights[0]<=weight:  sum을 쓰면 효율성이 낮아진다!!
        if now_weight+truck_weights[0]<=weight:
            now_weight+=truck_weights[0]
            on_bridge.append(truck_weights.popleft())
        else:
            on_bridge.append(0)

    answer+=len(on_bridge)

    return answer


if __name__ == "__main__":
    import time

    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]

    start = time.time()
    print(solution(bridge_length, weight, truck_weights))
    end = time.time()

    print(f"{end - start:.5f} sec")