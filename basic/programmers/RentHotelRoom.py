# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/155651

###############################
#           풀이 완료          #
###############################


## queue 이용하여 시간순 정렬 후 첫번째 방 예약 시간 맟춰서 pop -> heap 이용해서 정렬하면 더 빠르게 할 수 있을듯.
## 한바퀴 다 돌고 나면 다시 처음부터 돌면서 두번째 방 예약 맞춰서 pop
def solution(book_time):
    import datetime as dt
    answer = 0
    
    # 시간으로 변환
    book_time = sorted([[dt.datetime.strptime(time[0], '%H:%M'), dt.datetime.strptime(time[1], '%H:%M')] for time in book_time])
    # 예약 완료된 방을 표시하기 위한 dict
    check_register = {i: False for i in range(len(book_time))}
    print(check_register)

    while set(check_register.values())!=set([True]):
        for key in check_register.keys():
            if check_register[key]==False:
                [bf_start_time, bf_end_time] = book_time[key]
                check_register[key]=True
                break

        print(book_time)

        ##for문으로 한바퀴 돌면서 추가예약가능한 방이 있는지 체크
        ## 가능한 방이 있다면 check_register에서 True로 변경
        for (idx,[start_time, end_time]) in enumerate(book_time):
            # 종료시간에서 10분 이후가 다음날일 경우 추가대실 불가
            if bf_end_time>=dt.datetime.strptime('23:50', '%H:%M'):
                break
            ## 닫는시간 이후에 예약했을 경우, 닫는시간 이후에 예약했을 경우 pass
            elif start_time>=bf_end_time+dt.timedelta(minutes=10) and check_register[idx]==False:
                print(f"이전 예약시간 : {bf_start_time} ~ {bf_end_time}")
                print(f"예약성공 : {start_time} ~ {end_time}")
                bf_start_time = start_time
                bf_end_time = end_time
                check_register[idx]=True
                print(f"check_register : {check_register}")
                print("=="*20)
        answer+=1

    return answer

if __name__ == "__main__":
    import time
    book_time = [["00:01", "00:10"], ["00:13", "00:10"], ["04:00", "23:58"]]

    print("start")
    start = time.time()
    print(solution(book_time))
    end = time.time()

    print(f"{end - start:.5f} sec")
