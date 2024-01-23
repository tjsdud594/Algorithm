### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

###############################
#           풀이 중 - 시간초과          #
###############################


def solution(number, k):
    answer=''
    index=0
    number_list = list(number)


    while index<len(number_list)-1 and k>0:
        # print(number_list)
        # print(number_list[index], number_list[index+1], k)
        if number_list[index]<number_list[index+1]:
            number_list.pop(index)
            index=0
            k-=1
        else:
            index+=1

    if k>0:
        number_list = number_list[:-k]
    
    
    return ''.join(number_list)



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
    number = "4177252841"
    k=4

    print("start")
    start = time.time()
    print(solution(number, k))
    end = time.time()

    print(f"{end - start:.5f} sec")