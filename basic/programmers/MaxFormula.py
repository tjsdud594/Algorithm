# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/67257

###############################
#           풀이 완료          #
###############################

from itertools import permutations

def calc(num1, num2, operator):
    if operator == "*":
        return str(int(num1) * int(num2))
    elif operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))

def logic(exp, op):
    array = []
    tmp = ""

    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)

    for o in op:
        stack = []
        while len(array)!=0:
            tmp = array.pop(0)
            if tmp==o:
                stack.append(calc(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack

    return abs(int(array[0]))

def solution(expression):
    oper = permutations(["+", "-", "*"], 3)
    result = []
    for op in oper:
        result.append(logic(expression, op))

    return max(result)

if __name__ == "__main__":
    import time
    expression = "100-200*300-500+20"

    print("start")
    start = time.time()
    print(solution(expression))
    end = time.time()

    print(f"{end - start:.5f} sec")
