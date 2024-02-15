'''K번째 수
https://www.acmicpc.net/problem/1300

문제
세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.

입력
첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.

출력
B[k]를 출력한다.

예제 입력 1 
3
7
예제 출력 1 
6
'''
import sys
N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# 메모리 초과
def knum1(N, k):
    B = sorted([i*j for i in range(1, N+1) for j in range(1, N+1)])
    return B[k]

# print(knum1(N, k))


# 이분탐색 활용
def knum2(N, k):
    start = 1
    end = k
    while start<=end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1,N+1):
            cnt+=min(N, mid//i)

        if cnt>=k:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

print(knum2(N, k))

