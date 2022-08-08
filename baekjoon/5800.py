T = int(input())
for i in range(1, T+1):
    Class = list(map(int, input().split()))
    new_Class = Class[1:]
    new_Class = sorted(new_Class, reverse = True)
    result = 0
    for j in range(len(new_Class)):
        if j == len(new_Class) - 1:
            break
        if new_Class[j] - new_Class[j+1] > result:
            result = new_Class[j]-new_Class[j+1]
    print('Class', i)
    print(f'Max {max(new_Class)}, Min {min(new_Class)}, Largest gap {result}')
