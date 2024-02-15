### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42860

###############################
#           풀이 완료          #
###############################

def solution(name):
    from string import ascii_uppercase
    answer=float("inf")
    
    def control_cnt(cmd):
        if cmd=="":
            return 0
        cnt=0
        # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        alpha_dict = {alpha:i+1 for i, alpha in enumerate(ascii_uppercase)}

        for i in cmd:
            cnt+=min((alpha_dict[i]-1), (27-alpha_dict[i]))
            cnt+=1
        
        return cnt-1

    def find_min_cnt(name):  
        cnt = float("inf")  
        for i in range(len(name)+1):
            # print(f"i : {i}")
            front_name = name[:i].rstrip("A")
            back_name = name[i:]
            back_name = back_name[::-1].rstrip("A")
            print(front_name, control_cnt(front_name), len(front_name))
            print(back_name, control_cnt(back_name))

            if control_cnt(back_name)==0:
                back_control = 0
            else:
                if len(back_name)>0:
                    if len(front_name)==0:
                        back_control=len(front_name)+1
                    else:
                        back_control=len(front_name)
                else:
                    back_control=0
            print(f"back_control : {back_control}")
            cnt = min(cnt, control_cnt(front_name)+(control_cnt(back_name))+back_control)

            # answer+=control_cnt(front_name)
            # name = name[i:]+name[:i]
            print(cnt)
            print("==============================================================")

        return cnt 
    
    print(find_min_cnt(name), find_min_cnt(name[::-1])+1)

    return min(find_min_cnt(name), find_min_cnt(name[::-1])+1)

if __name__ == "__main__":
    import time
    import random

    name = "RCETAAAAVUEAETZAAAK"

    question_dict = data = {
    'LABLPAJM': 61,
    'BMOABA': 30,
    'LAABAA': 15,
    'AAAAAAAAJAAAA': 14,
    'SAAAAAARRM': 41,
    'RABAMATAWADLAFAVAAE': 78,
    'XAAAAAABA': 6,
    'AYOZAAVADAY': 35,
    'AAFEASAAVA': 30,
    'UAGAAASAAFAFXZA': 47,
    'AAAAZAATAEA': 19,
    'AACALATLAHABAA': 50,
    'FAWJAAAFV': 35,
    'AACAVAAPSAAOAA': 49,
    'AKAAWAKX': 33,
    'LOAAAHAJAAFAEBAWO': 79,
    'AWAWVAQVAAA': 35,
    'RCETAAAAVUEAETZAAAK': 75,
    'GTAASKKAE': 52,
    'AAAABAAAAAAKSAIQ': 49,
    'ADASAAAUAAAPAA': 39,
    'AAAAADBAAELSPUAAAOA': 70,
    'VJAAIAFNAAAAA': 47,
    'AARUAUAAHTBJAAYS': 69,
    'IASAGITUPHE': 74,
    'AAALAAAAAA': 14,
    'AAAEASAHQAYTAAAJ': 60,
    'BAALEAAAPMAAAHSRAV': 83,
    'ASWAAATDAJAXA': 45,
    'DYAOAAAARQANAWA': 66,
    'AAIAPB': 24
}

    # for q in question_dict.keys():
        # if question_dict[q]!=solution(q):
            # print(f"str : {q}, answer : {question_dict[q]}, wrong : {solution(q)}")
        # print(solution(q))
    
    start = time.time()
    print(solution(name))
    end = time.time()

    print(f"{end - start:.5f} sec")



