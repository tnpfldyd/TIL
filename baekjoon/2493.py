def main():
    N = int(input())
    tops = list(map(int, input().split()))
    stack = []
    answer = []
    for idx, top in enumerate(tops, 1):
        while stack and stack[-1][1] <= top:
            stack.pop()
        answer.append(0 if not stack else stack[-1][0])
        stack.append((idx, top))
    print(*answer)
if __name__ == "__main__":
    main()