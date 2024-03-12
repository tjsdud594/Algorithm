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



if __name__ == "__main__":
    import time
    prices = [1,2,3,2,3]

    print("start")
    start = time.time()
    print(solution(prices))
    end = time.time()

    print(f"{end - start:.5f} sec")