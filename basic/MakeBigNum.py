### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

###############################
#           풀이 완료          #
###############################


def solution_t(number, k):

    print(number, k)
    answer = []

    for num in number:
        if answer==[]:
            answer.append(num)
            continue
        elif answer[-1]<num and k>0:

            while answer[-1]<num and k>0:
                answer.pop()
                k-=1

                if k<=0 or answer==[]:
                    break
            answer.append(num)
            continue
        else:
            answer.append(num)

    if k>0:
        answer = answer[:-k]

    return ''.join(answer)


# 이전 풀이
def solution_bf(number, k):

    ans = []
    for num in number:
        if k==0:
            ans.append(num)
        elif ans==[]:
            ans.append(num)
            continue
        elif ans[-1]<num:
            while ans[-1]<num:
                
                ans.pop()
                k-=1
                if k==0 or not ans:
                    break
            ans.append(num)
        else:
            ans.append(num)
            continue
    if k>0:
        ans = ans[:-k]
    return "".join(ans)


if __name__ == "__main__":
    import time
    number = "654321"
    k=5

    print("start")
    start = time.time()
    print(solution_t(number, k))
    end = time.time()

    print(f"{end - start:.5f} sec")