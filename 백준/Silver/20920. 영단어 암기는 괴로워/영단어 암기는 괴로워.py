import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

word_list = [(freq, len(word), word) for word, freq in words.items()]
word_list.sort(key=lambda x: (-x[0], -x[1], x[2]))

for _, _, word in word_list:
    print(word)