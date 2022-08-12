import sys
from collections import Counter

# sys.stdin = open("input_text/_반반.txt")

T = int(input())

answer = 'Yes'
for test_case in range(1, T + 1):
    S = Counter(input())

    if len(S) != 2:
        answer = 'No'

    for cnt in S.values():
        if cnt != 2:
            answer = 'No'

    print(f'#{test_case} {answer}')