import sys
input = sys.stdin.readline

S = input().strip()

zero_count = S.count('0')
one_count = S.count('1')

remove_zero = zero_count // 2
remove_one = one_count // 2

result = []
for char in S:
    if char == '1' and remove_one > 0:
        remove_one -= 1
    else:
        result.append(char)

S = result
result = []

for i in range(len(S) - 1, -1, -1):
    if S[i] == '0' and remove_zero > 0:
        remove_zero -= 1
    else:
        result.append(S[i])

result.reverse()
print(''.join(result))