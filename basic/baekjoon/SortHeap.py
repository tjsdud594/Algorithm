### 문제 : https://www.acmicpc.net/problem/2220

###############################
#           풀이 완료          #
###############################

n=int(input())
heap = [0, 1]

## list 내부에서 자리 바꾸는 함수 
def swap(heap, a,b):
    temp = heap[a]
    heap[a] = heap[b]
    heap[b] = temp
    return heap

for i in range(2, n+1):
    # 순서대로 숫자를 append해서 추가
    print(f"append : {i}")
    heap.append(i)
    heap=swap(heap, i, i-1)
    print(heap)
    j = i-1 ## 현재 추가된 최대 값 위치 
    # append된 숫자를 부모노드와 값을 바꾸어가며 swap
    while j!=1:
        heap = swap(heap, j, j//2)
        print(heap)
        j = j//2

for i in heap[1:]:
    print(i, end=" ")



