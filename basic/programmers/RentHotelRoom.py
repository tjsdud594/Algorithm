# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/155651

###############################
#           풀이 완료          #
###############################


## queue 이용하여 시간순 정렬 후 첫번째 방 예약 시간 맟춰서 pop -> heap 이용해서 정렬하면 더 빠르게 할 수 있을듯.
## 한바퀴 다 돌고 나면 다시 처음부터 돌면서 두번째 방 예약 맞춰서 pop
def solution(book_time):
    import datetime as dt
    answer = 0

    for book in book_time:
        start = dt.datetime.strptime(book[0], '%H:%M')
        end = dt.datetime.strptime(book[1], '%H:%M') + dt.timedelta(minutes=10)
        print(start.time(), end.time())
    return answer

if __name__ == "__main__":
    import time
    book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

    print("start")
    start = time.time()
    print(solution(book_time))
    end = time.time()

    print(f"{end - start:.5f} sec")
