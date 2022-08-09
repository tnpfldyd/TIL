T = int(input())
list_ = [0] * 5
for i in range(T):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        list_[0] += 1
    elif x > 0 and y < 0:
        list_[3] += 1
    elif x < 0 and y > 0:
        list_[1] += 1
    elif x < 0 and y < 0:
        list_[2] += 1
    else:
        list_[4] += 1
for i in range(len(list_)):
    if i == 4:
        print(f'AXIS: {list_[i]}')
    else:
        print(f'Q{i+1}: {list_[i]}')
