### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/120956

###############################
#           풀이 완료          #
###############################

#효율성 비교
# (good)2>1>3(bad)



# 1 내 풀이법 조합 전부 생성후 set으로 비교
def solution(babbling):
    import itertools
    answer = 0
    cadidate = ["aya", "ye", "woo", "ma"]
    
    babblings_set = set([])
    for i in range(1,5):
        babblings_set = babblings_set.union({''.join(s) for s in list(itertools.permutations(cadidate, i))})

    
    for babb in babbling:
        if (set([babb]) & babblings_set):
            answer+=1
        else:
            pass
    
        
    return answer

# 2 내 풀이법 조합전부 생성하여 dictionary key로 지정 후 key값과 비교
def solution(babbling):
    import itertools
    answer = 0
    cadidate = ["aya", "ye", "woo", "ma"]
    
    babblings_dict = {}
    for i in range(1,5):
        for s in list(itertools.permutations(cadidate, i)):
            babblings_dict[''.join(s)]=True
    
    for babb in babbling:
        if (babb in babblings_dict.keys()):
            answer+=1
        else:
            pass
        
    return answer


# 3 정규표현식으로 풀기
def solution(babbling):
    import re
    answer=0
    
    regex = re.compile(f'^(aya|ye|woo|ma)+$')
    for babb in babbling:
        if (regex.match(babb)):
            answer+=1
        
    return answer