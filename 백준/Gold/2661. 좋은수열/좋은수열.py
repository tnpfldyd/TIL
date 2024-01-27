N = int(input())

def solve(tmp):
    
    size = len(tmp)
    for i in range(1, size // 2 + 1):
        if tmp[size - i:size] == tmp[size - 2 * i:size - i]:
            return
    
    if size == N:
        print(tmp)
        exit()
    
    for i in range(N):
        solve(tmp + "1")
        solve(tmp + "2")
        solve(tmp + "3")

solve("")