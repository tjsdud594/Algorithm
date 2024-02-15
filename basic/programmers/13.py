'''
[문제 설명]
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

[제한사항]
N의 범위 : 100,000,000 이하의 자연수

[입출력 예]
N	answer
123	6
987	24

[입출력 예 설명]
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.
'''

n = 987
# int 타입은 len()을 쓰지 못함!!
# print(str(n))   # int 타입인 n을 str로 바꾸어서 len()실행

# solution 1
def solution(n):
    answer = 0
    for i in range(0,len(str(n))):
        answer += int(str(n)[i])

    return answer


# solution 2 (재귀함수)
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)


print(solution(n))


# solution 2
