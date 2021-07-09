<!--이모지 : https://steemit.com/steemkr-guide/@snow-airline/steemkr-quick-start-guide-->
<!--이모지 넣는 방법 윈도우키+마침표-->


## &#128187;Algorithm Code를 공부한 흔적들입니다!

### 1주차. Stack / Queue
<details>
<summary>&#128200;주식가격</summary>
 &nbsp; &nbsp; > 해결&#128515;

    def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):                          
            if prices[i] > prices[j]:  
                answer[i] += 1  
                break
            else:
                answer[i] += 1
    return answer
   </details>

<details>
> <summary>기능개발</summary>
    해결&#10060;
   </details>
<details>
> <summary>다리를 지나는 트럭</summary>
    해결&#10060;
   </details>
    