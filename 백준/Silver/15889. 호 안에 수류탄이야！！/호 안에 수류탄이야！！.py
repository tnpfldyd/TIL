import sys
input = sys.stdin.readline

N = int(input().strip())
pos = list(map(int, input().split()))

if N == 1:
    print("권병장님, 중대장님이 찾으십니다")

else:
    rng = list(map(int, input().split()))

    max_reach = pos[0] + rng[0]

    for i in range(1, N):
        if pos[i] > max_reach:
            print("엄마 나 전역 늦어질 것 같아")
            break
        if i < N - 1:
            max_reach = max(max_reach, pos[i] + rng[i])
    else:
        print("권병장님, 중대장님이 찾으십니다")