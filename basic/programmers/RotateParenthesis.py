# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

###############################
#           풀이 완료          #
###############################


def solution(s):
    answer = 0
    for idx in range(len(s)):
        tmp_s = s[idx:]+s[:idx]
        while 1:
            length = len(tmp_s)
            tmp_s = tmp_s.replace("()", "")
            tmp_s = tmp_s.replace("{}", "")
            tmp_s = tmp_s.replace("[]", "")
            if len(tmp_s)==0:
                answer+=1
                break
            if length==len(tmp_s):
                break
    return answer

if __name__ == "__main__":
    import time
    s = "{}([])"

    print("start")
    start = time.time()
    print(solution(s))
    end = time.time()

    print(f"{end - start:.5f} sec")
