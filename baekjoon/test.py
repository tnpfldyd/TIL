# 오른쪽, 위쪽, 왼쪽, 아래쪽
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

n = int(input())

# 표본 모양수열을 만들 숫자 리스트
sample = list(map(int, input().split()))

# 표본 모양수열의 위치 좌표 리스트
sample_list = []

# 기준 좌표 설정
r, c = (0, 0)

for i in range(n):
    sample_list.append([r, c])
    r += dr[sample[i]-1]
    c += dc[sample[i]-1]

sample_list = sorted(sample_list)

rst = []
cnt = 0
for _ in range(int(input())):
    sample_ = list(map(int, input().split()))
    # 표본 모양모방수열의 위치 좌표 리스트
    sample_list_ = []

    # 기준 좌표 설정
    r, c = (0, 0)

    for i in range(n):
        sample_list_.append([r, c])
        r += dr[sample_[i]-1]
        c += dc[sample_[i]-1]
    
    min_ = min(sample_list_)
    # 기준점 (0, 0)에 맞춰서 좌표들의 값 수정.
    if min_ != [0, 0]:
        y = min_[0]
        x = min_[1]

        for i in range(n):
            sample_list_[i][0] -= y
            sample_list_[i][1] -= x
    new_sample_list_ = sorted(sample_list_)

    if new_sample_list_ == sample_list:
        rst.append(sample_)
        cnt += 1

print(cnt)
for i in rst:
    print(*i)