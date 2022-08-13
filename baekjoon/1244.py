T = int(input())
switch = list(map(int, input().split()))
N = int(input())
for i in range(N):
    command, idx = map(int, input().split())
    if command == 1:
        stack = [idx]
        while stack:
            trade = stack.pop()
            if trade <= T:
                switch[trade - 1] = abs(switch[trade - 1] - 1)
                trade += idx
                stack.append(trade)
    else:
        if 0 <= idx - 2 and idx < T:
            if switch[idx - 2] == switch[idx]:
                switch[idx - 1] = abs(switch[idx - 1] - 1)
                start = [(idx - 2, idx)]
                while start:
                    left, right = start.pop()
                    if 0 <= left and right < T:
                        if switch[left] == switch[right]:
                            switch[left] = abs(switch[left] - 1); switch[right] = abs(switch[right] - 1)
                            start.append((left - 1, right + 1))
            else:
                switch[idx - 1] = abs(switch[idx - 1] - 1)
        else:
            switch[idx - 1] = abs(switch[idx - 1] - 1)
for i in range(T):
    if i % 20 == 0:
        print(*switch[i:i + 20])