import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    words = [input().strip() for _ in range(k)]
    found = False
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            s = words[i] + words[j]
            if s == s[::-1]:
                print(s)
                found = True
                break
        if found:
            break
    if not found:
        print(0)