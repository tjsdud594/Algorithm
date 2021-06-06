'''
<문제 설명>
    초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

    *제한사항
        prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
        prices의 길이는 2 이상 100,000 이하입니다.

    *입출력 예
        prices	        return
        [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

    *입출력 예 설명
        1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
        2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
        3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
        4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
        5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''

# 파이썬 튜토리얼로 차근차근 생각해보기!!

prices = [1, 2, 3, 2, 3]

# Solution1 - for
def solution(prices):
    answer = [0] * len(prices)   #len(prices) : 5
    
    for i in range(len(prices)-1):   #range(5-1) = range(4) = 0, 1, 2, 3 범위
        for j in range(i, len(prices)-1):    # i = 0 일땐 j in range(0, 4) -> j = 0, 1, 2, 3 -> prices[0] > prices[0,1,2,3] -> answer = 1+1+1+1
            if prices[i] > prices[j]:    
                break
            else:
                answer[i] += 1
    return answer

print(solution(prices))

prices = [1, 2, 3, 2, 3]

# Solution2 - for문 이용해서 더 잘 이해할 수 있게 수정해보기!!!
def solution(prices):
    answer = [0] * len(prices)   #len(prices) : 5
    
    for i in range(len(prices)):   # i는 range(5) = 0, 1, 2, 3, 4 범위
        for j in range(i+1, len(prices)):    # i = 0 일땐 j in range(1, 5) -> j = 1, 2, 3, 4 -> prices[0]1 > prices[1,2,3,4]2323 (else)-> answer = 1+1+1+1 = 4
                                             # i = 1 일땐 j in range(2, 5) -> j = 2, 3, 4 -> prices[1]2 > prices[2, 3, 4]323 (else)-> answer = 1+1+1 = 3
                                             # i = 2 일땐 j in range(3, 5) -> j = 3, 4 -> prices[2]3 > prices[3, 4]23 ->break (answer = 1)
                                             # i = 3 일땐 j in range(4, 5) -> j = 4 -> prices[3]2 > prices[4]3 (else)-> answer = 1
                                             # i = 4 일땐 j in range(5, 5) -> j = 존재하지 않으므로 상위 for문으로 돌아감 -> i의 범위가 끝났으므로 answer을 리턴 따라서 answer의 마지막 값은 0가 유지됨.
            if prices[i] > prices[j]:  
                answer[i] += 1  
                break
            else:
                answer[i] += 1
    return answer

print(solution(prices))
