import sys
S, T = list(input()), list(input())
N = len(S)
def search(arr):
    if len(arr) == N:
        if arr == S:
            print(1)
            sys.exit()
        return
    if arr[0] == 'B':
        temp = arr.copy()
        temp.reverse()
        temp.pop()
        search(temp)
    if arr[-1] == 'A':
        temp = arr.copy()
        temp.pop()
        search(temp)

search(T)
print(0)