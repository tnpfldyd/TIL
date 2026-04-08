a = input().strip()
b = input().strip()

count_a = [0] * 26
count_b = [0] * 26

for ch in a:
    count_a[ord(ch) - ord('a')] += 1

for ch in b:
    count_b[ord(ch) - ord('a')] += 1

answer = 0
for i in range(26):
    answer += abs(count_a[i] - count_b[i])

print(answer)