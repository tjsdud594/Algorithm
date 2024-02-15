'''가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
'''
n = int(input())
lst = list(map(int, input().split()))
''' 
반례
5
1 4 2 3 5

num = Nlist[0]
if cnt==1:
    print(1)
for i in range(1,cnt):
    if Nlist[i]>num:
        dp[i] = max(dp[:i]) + 1
        num = Nlist[i]
print(max(dp))
'''
# https://11001.tistory.com/143
# 2중 for 문을 이용해 전부 비교해서 dp값 저장
def LIS1(lst, n):
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if lst[i]>lst[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

# 이진탐색을 활용한 1중 for 문 해결(LIS1 방식보다 3배 빠르다!!)
import bisect, sys
def LIS2(lst, n):
    inc_arr = [sys.maxsize] * n
    for i in range(0, n):
        idx = bisect.bisect_left(inc_arr, lst[i])
        inc_arr[idx] = lst[i]

    return bisect.bisect_left(inc_arr, sys.maxsize)