# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/67257

###############################
#           풀이 완료          #
###############################

from itertools import permutations

def cal(op, a, b):
    a = int(a)
    b = int(b)
    if op=="-":
        return str(a-b)
    elif op=="+":
        return str(a+b)
    else:
        return str(a*b)
    
def oper(expression, op_list):
    cal_list = []
    tmp = ""

    ## 숫자와 연산자 구분하여 list 생성 -> cal_list = ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    for num in expression:

        if num.isdigit()==True:
            tmp+=num
        else:
            cal_list.append(tmp)
            cal_list.append(num)
            tmp=""
    cal_list.append(tmp)

    ## stack구조를 활용해서 순서대로 계산 
    for op in op_list:
        stack = []
        while len(cal_list)!=0:
            tmp = cal_list.pop(0)

            ## 연산자 차례일경우 계산
            if tmp==op:
                stack.append(cal(op, stack.pop(), cal_list.pop(0)))
            else:
                stack.append(tmp)
        cal_list=stack
    return abs(int(cal_list[0]))

def solution(expression):
    answer = []
    op_permu = list(permutations(("+","-","*"), 3))

    for op_list in op_permu:
        answer.append(oper(expression, op_list))
    
    return max(answer)

if __name__ == "__main__":
    import time
    expression = "100-200*300-500+20"

    print("start")
    start = time.time()
    print(solution(expression))
    end = time.time()

    print(f"{end - start:.5f} sec")
