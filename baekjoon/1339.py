from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
alpha_dic = defaultdict(int)
for _ in range(N):
    alpha = input().strip()
    length = len(alpha)
    for i in range(length):
        alpha_dic[alpha[i]] += 10 ** (length - i - 1)

alpha_dic = sorted(alpha_dic.items(), key=lambda x : -x[1])

res = 0
cnt = 9
for alpha in alpha_dic:
    res += alpha[1] * cnt
    cnt -= 1
print(res)