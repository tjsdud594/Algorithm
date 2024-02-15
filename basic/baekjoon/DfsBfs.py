### 문제 : https://www.acmicpc.net/problem/1260

###############################
#           풀이 중          #
###############################


# 재귀함수 (종료조건을 확실하게 할 것!!)
# dfs 수정필요!!!
def dfs(nodes, node_lines1, start_node1, answer1):
    # if len(answer1)==nodes or node_lines1==[]:
    if len(answer1)==nodes:
        return " ".join(list(map(str, answer1)))
    
    else: 
        if start_node1 not in answer1:
            answer1.append(start_node1)

        if len(answer1)<nodes:
            for line in node_lines1:
                if start_node1 in line:
                    node_lines1.remove(line)
                    line.remove(start_node1)

                    if line[0] not in answer1:
                        start_node1 = line[0]
                        answer1.append(start_node1)
                        print(f"dfs answer1 : {answer1}")

                    dfs(nodes, node_lines1, start_node1, answer1)
                    return " ".join(list(map(str, answer1)))



def bfs(node_lines2, start_node2):
    
    visit_node = [start_node2]
    answer2 = [start_node2]

    while visit_node!=[]:

        node = visit_node.pop(0)
        non_visit = []
        
        for line in node_lines2:
            if node in line:
                line.remove(node)

                if line[0] not in answer2:
                    visit_node.append(line[0])
                    answer2.append(line[0])

            else:
                non_visit.append(line)

        node_lines2 = non_visit
    return " ".join(list(map(str, answer2)))


if __name__ == "__main__":
    import copy
    [nodes, lines, start_node] = list(map(int, input().split()))

    # global node_lines1, node_lines2
    node_lines1 = []
    node_lines2 = []

    for _ in range(lines):
        line = list(map(int, input().split()))
        node_lines1.append(copy.deepcopy(line))
        node_lines2.append(copy.deepcopy(line))

    start_node1 = copy.deepcopy(start_node)
    node_lines1.sort(key = lambda x:(x[0], x[1]))
    answer1=list()
    print(dfs(nodes, node_lines1, start_node1, answer1))

    start_node2 = copy.deepcopy(start_node)
    node_lines2.sort(key = lambda x:(x[0], x[1]))
    answer2=list()
    print(bfs(node_lines2, start_node2))



