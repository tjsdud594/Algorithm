'''
[문제 설명]
[프렌즈4블록]
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

http://t1.kakaocdn.net/welcome2018/pang1.png
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

http://t1.kakaocdn.net/welcome2018/pang2.png
블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

http://t1.kakaocdn.net/welcome2018/pang3.png
만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

http://t1.kakaocdn.net/welcome2018/pang4.png
위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

[입력 형식]
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

[출력 형식]
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

입출력 예제
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
[예제에 대한 설명]
입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
입출력 예제 2는 본문 설명에 있는 그림을 옮긴 것이다. 11개와 4개의 블록이 차례로 지워지며, 모두 15개의 블록이 지워진다.
'''

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

def solution(m, n, board):
    answer = 0
    check = [[0]*n for _ in range(m)]
    board = [list(i) for i in board]

    while 1:
        cnt = 0
        for i in range(m-1):
            for j in range(n-1):
                # 2*2형태로 블록이 있다면 체크리스트에 1로 표시하기
                if board[i][j]!=1 and board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]:
                    check[i][j], check[i+1][j], check[i][j+1], check[i+1][j+1] = 1,1,1,1
                    cnt+=1
        print("board는 그대로 : ", board)
        print("check만 표시 : ",check)
        if cnt==0:
            break
        # check에 1로 표시된 블록을 1로 표시해서 삭제하기
        for i in range(m):
            for j in range(n):
                if check[i][j]==1:
                    board[i][j] = 1

        print("board도 표시 : ", board)
        print("check만 표시 : ",check)
        # 삭제 후 위의 블럭들 아래로 내림
        for i in range(m-1, -1, -1):
            for j in range(n):
                # 아래에서부터 올라오면서 1이(지워진 블록) 있으면
                if board[i][j]==1:
                    x = i
                    while x>0:
                        x-=1
                        if x<0:
                            break
                        if board[x][j]!=1:
                            board[i][j] = board[x][j]
                            board[x][j] = 1
                            check[i][j] = 0
                            check[x][j] = 1

        print(board)
        print(check)
    return sum([i.count(1) for i in board])
    
print(solution(m, n, board))