import sys

def get_min_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

unique_words = set(get_min_rotation(word) for word in words)

print(len(unique_words))