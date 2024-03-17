from collections import defaultdict
import sys
input = sys.stdin.readline

def parse(word):
    if len(word) > 3:
        return word[0] + ''.join(sorted(word[1:-1])) + word[-1]
    return word
N = int(input())
words_map = defaultdict(int)

for _ in range(N):
    word = input().strip()
    new_word = parse(word)
    words_map[new_word] += 1
M = int(input())
for _ in range(M):
    answer = 1
    words = input().strip().split()
    flag = False
    for word in words:
        new_word = parse(word)
        if new_word in words_map:
            flag = True
            answer *= words_map[new_word]
    print(answer if flag else 0)