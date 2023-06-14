from collections import defaultdict
order_dic = {}
cnt_dic = defaultdict(int)

N, C = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    if number not in order_dic:
        order_dic[number] = cnt
        cnt += 1
    cnt_dic[number] += 1

numbers.sort(key=lambda x : (-cnt_dic[x], order_dic[x]))

print(*numbers)