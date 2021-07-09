prices = [1, 2, 3, 2, 3, 3, 2]

# Solution1 - for문 이용해서 수정해보기!!!
def solution(prices):
    answer = [0] * len(prices)   #len(prices) : 5
    
    for i in range(len(prices)):   # i는 range(5) = 0, 1, 2, 3, 4 범위
        for j in range(i+1, len(prices)):    # i = 0 일땐 j in range(1, 5) -> j = 1, 2, 3, 4 -> prices[0]1 > prices[1,2,3,4]2323 (else)-> answer = 1+1+1+1 = 4
                                             # i = 1 일땐 j in range(2, 5) -> j = 2, 3, 4 -> prices[1]2 > prices[2, 3, 4]323 (else)-> answer = 1+1+1 = 3
                                             # i = 2 일땐 j in range(3, 5) -> j = 3, 4 -> prices[2]3 > prices[3, 4]23 ->break (answer = 1)
                                             # i = 3 일땐 j in range(4, 5) -> j = 4 -> prices[3]2 > prices[4]3 (else)-> answer = 1
                                             # i = 4 일땐 j in range(5, 5) -> j = 존재하지 않으므로 상위 for문으로 돌아감 -> i의 범위가 끝났으므로 answer을 리턴 따라서 answer의 마지막 값은 0가 유지됨.
            if prices[i] > prices[j]:  
                answer[i] = 1  
                break
            else:
                answer[i] += 1
    return answer

print(solution(prices))

