'''
[문제 설명]
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,/ 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,/ 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,/ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

[제한 조건]
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

[입출력 예]
answers	    return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]

[입출력 예 설명]

입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
'''
from itertools import chain, repeat
import operator

answer = [1,2,3,4,5]

def solution(answers):
    A = [1,2,3,4,5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    A_answer = list(chain.from_iterable(repeat(A,int(10000/len(A)))))
    B_answer = list(chain.from_iterable(repeat(B,int(10000/len(B)))))
    C_answer = list(chain.from_iterable(repeat(C,int(10000/len(C)))))

    a=0
    b=0
    c=0

    for ques in range(len(answers)):
        if A_answer[ques] == answers[ques]:
            a+=1
        if B_answer[ques] == answers[ques]:
            b+=1
        if C_answer[ques] == answers[ques]:
            c+=1

    answer = [a,b,c]

    ans_list =  list(filter(lambda x: answer[x] == max(answer), range(len(answer))))
    return list(map(operator.add, ans_list, [1,1,1]))

print(solution(answer))