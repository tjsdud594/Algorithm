### 문제 : https://www.acmicpc.net/problem/1764

###############################
#           풀이중           #
###############################

from collections import defaultdict
import sys 

N, M = map(int, sys.stdin.readline().split())
name_list=[]
name_dict=defaultdict(int)

for i in range(N+M):
    name = sys.stdin.readline().rstrip('\n')
    name_dict[name]+=1
    if name_dict[name]==2:
        name_list.append(name)

print(len(name_list))
name_list = sorted(name_list)
for n in name_list:
    print(n)
