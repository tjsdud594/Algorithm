### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/178870

###############################
#           풀이완료           #
###############################

def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    num=sequence[start]

    while end<=len(sequence)-1 and start<=len(sequence)-1:
        print(f"start : {start}, end : {end}, num : {num}")
        if num == k:
            answer.append([start, end, end-start])
            if start==len(sequence)-1:
                break
        if num<=k:
            if end<len(sequence)-1:
                end+=1
                num+=sequence[end]
            else:
                break
        elif num>k:
            num-=sequence[start]
            start+=1

    # print(answer)
    # print(sorted(answer, key= lambda x : x[2])[0][:2])
    return sorted(answer, key= lambda x : x[2])[0][:2]

if __name__ == "__main__":
    import time

    sequence = [2, 2, 2, 2, 2]
    k = 6

    start = time.time()
    print(solution(sequence, k))
    end = time.time()

    print(f"{end - start:.5f} sec")