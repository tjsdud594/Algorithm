'''
[문제 설명]
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

[제한 조건]
n은 2이상 1000000이하의 자연수입니다.

[입출력 예]
n	result
10	4
5	3

[입출력 예 설명]
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

# 답은 맞췄으나 효율성 통과X
# 소수가 아닌수들을 리스트에 담아서 n에서 그 수만큼 빼줌
def solution(n):
    lst = []
#     k는 절반까지의 수, i는 1씩 증가하면서 n보다 작은수를 만들도록 곱해주는수
    k = 2
    i = 2
    while k<=n//2:
        if k*i<=n:
            lst.append(k*i)
            i+=1
        else:
            i=2
            k+=1
    lst = list(set(lst))
        
    return n-len(lst)-1


# 에라토스테네스의 체 활용(효율성 통과X)
def solution2(n):
    not_prime = 0
    lst = list(range(2, n+1))
    for i in range(len(lst)):
        if lst[i]==2:
            not_prime-=1
        if lst[i]%2==0:
            not_prime+=1
        else:
            for j in range(2, int(lst[i]**0.5)+1):
                if lst[i]%j==0:
                    not_prime+=1
                    break
        
    return n-not_prime-1

# 효율성 통과
def solution3(n):
    lst = [True]*(n+1)
    lst[0] = False
    lst[1] = False
    for i in range(2, int(n**0.5)+1):
        if lst[i]==True:
            # 배수들 걸러냄
            for j in range(i+i, n+1, i):
                lst[j]=False
    # print([x for x in range(2, n+1) if lst[x]==True])
    return lst.count(True)