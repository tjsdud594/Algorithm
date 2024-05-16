### 문제 : https://www.acmicpc.net/problem/2220

###############################
#           풀이 완료          #
###############################

import heapq

n=int(input())
# answer = []
heap = [0, 1]

def swap(arr, x, y): #두 위치를 바꾸는 코드
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
 
for i in range(2, n+1):
    heap.append(i) #맨 뒤에 최댓값 추가
    swap(heap, i, i-1) #1과 바꿔줌
    j = i-1 #j위치에 있는 최댓값
    while j != 1: #j위치에 있는 최댓값은 최상단에 위치할 때 까지 부모 노드와 지속적으로 바꾸어줌
        swap(heap, j, j//2) #교환
        j = j//2 #부모 노드의 위치
        print(heap)

for i in heap[1:]:
    print(i, end = ' ')



