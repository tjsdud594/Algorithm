### 문제 : https://www.acmicpc.net/problem/10816

###############################
#           풀이완료           #
###############################

from collections import defaultdict, Counter
import sys
card_dict = defaultdict(int)
s_card_dict = defaultdict(int)
answer = ''

N = sys.stdin.readline()
cards = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()
s_cards = list(map(int, sys.stdin.readline().split()))

card_dict = Counter(cards)
for s_card in s_cards:
    print(card_dict[s_card], end=' ')