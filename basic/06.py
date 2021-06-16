arr = [1, 1, 3, 3, 0, 1, 1] 

# solution1
def solution(arr):
    answer = []
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[len(arr)-1])
            
    return answer

# solution2
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]:
            continue
        answer.append(i)

    return answer
