import sys
input = sys.stdin.readline

def is_good_word(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0

N = int(input())
count = 0

for _ in range(N):
    word = input().strip()
    if is_good_word(word):
        count += 1

print(count)