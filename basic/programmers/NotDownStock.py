### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42584

###############################
#           풀이 완료          #
###############################

# for + while
def solution(prices):
    answer = []

    for i in range(len(prices)-1):
        sec=0
        now = prices[i]
        j = i
        f = prices[j]

        while f>=now and j<len(prices):
            f = prices[j]
            sec+=1
            j+=1

        answer.append(sec-1)

    answer.append(0)

    return answer

# for+for : 효율성이 이 방법이 더 좋다!!
def solution2(prices):
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):

            if prices[j]>=prices[i]:
                answer[i]+=1
            else:
                answer[i]+=1
                break

    return answer


if __name__ == "__main__":
    import time
    prices = [1,2,3,2,3]

    print("start")
    start = time.time()
    print(solution2(prices))
    end = time.time()

    print(f"{end - start:.5f} sec")