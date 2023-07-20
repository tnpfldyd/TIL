import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = input().strip()
    K = int(input())
    alpha_cnt = [0] * 26
    for s in string:
        alpha_cnt[ord(s) - ord('a')] += 1
    min_answer = sys.maxsize
    max_answer = 0
    for i in range(len(string)):
        if alpha_cnt[ord(string[i]) - ord('a')] < K:
            continue
        cnt = 0
        for j in range(i, len(string)):
            if string[i] == string[j]:
                cnt += 1
            if cnt == K:
                min_answer = min(min_answer, j - i + 1)
                max_answer = max(max_answer, j - i + 1)
                break
    if min_answer == sys.maxsize or not max_answer:
        print(-1)
    else:
        print(min_answer, max_answer)