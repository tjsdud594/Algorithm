### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43163

###############################
#           풀이 완료          #
###############################

def solution(begin, target, words):

    if set([target])&set(words)==set():
        return 0
    
    else:
        answer = 0
        super_node = [begin]
        visit_node = {x: False for x in words}

        while set(super_node)&set([target])==set():
            tmp_node = []
            for node in super_node:
                for V in [n for n in visit_node.keys() if visit_node[n]==False]:
                    if [True if a==b else False for (a, b) in zip(node, V)].count(False)==1 and visit_node[V]==False:
                        visit_node[V]=True
                        tmp_node.append(V)
            
            answer+=1
            super_node=tmp_node

        return answer
    
if __name__ == "__main__":
    import time
    begin = "aab"
    target = "aba"
    words = ["abb", "aba"]

    print("start")
    start = time.time()
    print(solution(begin, target, words))
    end = time.time()

    print(f"{end - start:.5f} sec")



