import sys
input = sys.stdin.readline

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

asumb, csumd = [], []

for i in range(N):
    for j in range(N):
        asumb.append(numbers[i][0] + numbers[j][1])
        csumd.append(numbers[i][2] + numbers[j][3])

asumb.sort(); csumd.sort()

ab, cd = 0, len(csumd) - 1
answer = 0
while ab < N * N and cd >= 0:
    if not asumb[ab] + csumd[cd]:
        origin = ab
        same_ab = same_cd = 0
        while not asumb[ab] + csumd[cd]:
            same_ab += 1
            ab += 1
            if ab >= N * N:
                break
        while not asumb[origin] + csumd[cd]:
            same_cd += 1
            cd -= 1
            if cd < 0:
                break
        answer += same_ab * same_cd
    elif asumb[ab] + csumd[cd] < 0:
        ab += 1
    else:
        cd -= 1
print(answer)