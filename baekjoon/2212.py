n, k = int(input()), int(input())

if k >= n:
    print(0)
else:
    sensor = list(map(int, input().split()))
    sensor.sort()
    diffArr = [sensor[i+1] - sensor[i] for i in range(n-1)]
    diffArr.sort(reverse=True)
    sum = sum(diffArr[k-1:])
    print(sum)