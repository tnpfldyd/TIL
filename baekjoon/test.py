N = int(input())
list_ = list(map(int, input().split()))

max_len = 0

for i in range(len(list_) - 1):
    temp_len = 0
    temp = list_[i]

    for j in range(i + 1, len(list_)):
        if list_[j] > temp:
            temp = list_[j]
            temp_len += 1

    if temp_len >= max_len:
        max_len = temp_len

print(max_len)