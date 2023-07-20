N = int(input())
arr = [0] + list(map(int, input().split()))

result = []

def check(origin, target, n, order):
    arr = origin.copy()
    cnt = 0
    while target != n:
        for i in range(target, n+1) if order else range(target, n-1, -1):
            if target == arr[target]:
                break
            if arr[i] == target:
                cnt += 1
                reverse(arr, target, i) if order else reverse(arr, i, target)
                result.append(f"{target} {i}\n") if order else result.append(f"{i} {target}\n")
        target += 1 if order else -1
    if cnt == 1 or cnt == 2:
        return True
    else:
        return False
def reverse(arr, s, e):
    arr[s:e+1] = reversed(arr[s:e+1])

def output(result):
    if result:
        if len(result) == 1:
            print(1, 1)
            print(*result)
        else:
            print(''.join(result))
    else:
        print(1, 1)
        print(1, 1)
if check(arr, 1, N, True):
    output(result)
else:
    result = []
    check(arr, N, 1, False)
    output(result)
