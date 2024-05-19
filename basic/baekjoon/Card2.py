### 문제 : https://www.acmicpc.net/problem/2164

###############################
#           풀이 완료          #
###############################

input_card = int(input())

from collections import deque

cards = deque([n for n in range(1, input_card+1)])
answer=0

while cards:
    if len(cards)==1:
        answer=cards.pop()
        break
    else:
        cards.popleft()
        first = cards.popleft()
        cards.append(first) 

print(answer)   


