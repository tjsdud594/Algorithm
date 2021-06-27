'''
[문제 설명]
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

[제한 사항]
두 수는 1이상 1000000이하의 자연수입니다.

[입출력 예]
n	m	return
3	12	[3, 12]
2	5	[1, 10]

[입출력 예 설명]
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
'''

n = 3
m = 12

# solution 1
def solution(n, m):
    answer = []
    answer1 = []
    answer2 = []
    if n < m:
        for big in range(1, m+1):
            if m % big == 0 and n % big == 0:
                answer.append(big)
        a = answer.pop()
        answer2.append(a)

        for multi in range(n, n*m+1):
            if multi % n == 0 and multi % m == 0:
                answer1.append(multi)
        b = answer1.pop(0)
        answer2.append(b)

    elif n >= m:
        for big in range(1, n+1):
            if m % big == 0 and n % big == 0:
                answer.append(big)
        a = answer.pop()
        answer2.append(a)

        for multi in range(n, n*m+1):
            if multi % n == 0 and multi % m == 0:
                answer1.append(multi)
        b = answer1.pop(0)
        answer2.append(b)

    else:
        answer2 = [n, n]

    return answer2

# solution 2
def solution(a, b):
    mx, mn = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = mx % mn     # t는 최댓값을 최솟값으로 나눈 나머지
        mx, mn = mn, t    # 최댓값 = 최솟값 이 되고 최솟값 = t 가 됨
    answer = [mx, int(a*b/mx)]   # t = 0 이 될 경우 형성됨/ 최댓값 = 최솟값 이 최대공약수가 된다.

    return answer


print(solution(n, m))