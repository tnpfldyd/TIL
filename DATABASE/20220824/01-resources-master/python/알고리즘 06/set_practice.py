S = [
    "baekjoononlinejudge", "startlink", 
    "codeplus", "sundaycoding", "codingsh"
]

words = [
    "baekjoon", "codeplus", "codeminus", "startlink", "starlink", 
    "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"
]

# 풀이 1
cnt = 0

word_set = set(S)

for word in words:
    if word in set(S):
        cnt += 1

print(cnt)

# 풀이 2

print(len(set(words) & set(S)))