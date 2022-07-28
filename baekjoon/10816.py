import sys
input = sys.stdin.readline

T = int(input())
card_dic = {}
card = list(map(int, input().split()))
for i in card:
    if i not in card_dic:
        card_dic[i] = 1
    else:
        card_dic[i] += 1
T2 = int(input())
card_check = list(map(int, input().split()))
for j in card_check:
    print(card_dic.get(j, '0'), end = ' ')