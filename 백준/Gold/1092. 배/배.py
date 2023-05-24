N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
    exit()

ans = 0

while box:
    idx = 0
    i = 0
    while i < N:
        if idx == len(box):
            break
        elif crane[i] >= box[idx]:
            box.pop(idx)
            i += 1
        else:
            idx += 1
    ans += 1

print(ans)