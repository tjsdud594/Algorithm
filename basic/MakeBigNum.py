### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

###############################
#           풀이 완료          #
###############################


def solution(number, k):

    answer_list = []

    for i, n in enumerate(list(number)):
        if answer_list==[]:
            answer_list.append(n)

        elif int(answer_list[-1])>=int(n):
            answer_list.append(n)

        elif int(answer_list[-1])<int(n) and k>0:
            while int(answer_list[-1])<int(n) and k>0:
                # print(f"제거 진입, k:{k}, answer_list : {answer_list}, n: {n}")
                answer_list.pop()
                k-=1
                if answer_list==[] or int(answer_list[-1])>=int(n) or k==0:
                    answer_list.append(n)
                    break

        if k<=0:
            # print(f"k없음, k : {k}, answer_list : {answer_list}, list_num:{list(number)[i+1:]}")
            answer_list.extend(list(number)[i+1:])
            break

    if k>0:
        answer_list = answer_list[:-k]

    return ''.join(answer_list)



if __name__ == "__main__":
    import time
    number = "4177252841"
    k=4

    print("start")
    start = time.time()
    print(solution(number, k))
    end = time.time()

    print(f"{end - start:.5f} sec")