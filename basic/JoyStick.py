### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42860

###############################
#           풀이중           #
###############################

def solution(name):
    answer=float("inf")
    
    def control_cnt(cmd):
        if cmd=="":
            return 0
        cnt=0
        alpha_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "Y":24, "X":25, "Z":26}
        for i in cmd:
            cnt+=min((alpha_dict[i]-1), (27-alpha_dict[i]))
            cnt+=1
        
        return cnt-1

    
    for i in range(len(name)):
        # print(f"i : {i}")
        front_name = name[:i].rstrip("A")
        back_name = name[i:]
        back_name = back_name[::-1].rstrip("A")
        # print(front_name, control_cnt(front_name), len(front_name))
        # print(back_name, control_cnt(back_name))

        if control_cnt(back_name)==0:
            back_control = 0
        else:
            if i==0:
                back_control=max(0,i+1)
            else:
                back_control=max(0,i)
        # print(f"back_control : {back_control}")
        answer = min(answer, control_cnt(front_name)+(control_cnt(back_name))+back_control)

        # answer+=control_cnt(front_name)
        # name = name[i:]+name[:i]
        # print(answer)
        # print("==============================================================")

    return answer

if __name__ == "__main__":
    import time
    import random

    name = "JAZ"

    start = time.time()
    print(solution(name))
    end = time.time()

    print(f"{end - start:.5f} sec")



