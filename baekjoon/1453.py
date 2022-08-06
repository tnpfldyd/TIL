T = int(input())
num = list(map(int, input().split()))
num_set = set(num)
print(len(num)-len(num_set))