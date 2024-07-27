import sys
sys.setrecursionlimit(10 ** 6)

def cal(x, y, index, cnt, v, ans):
    if index == len(v):
        if ans[0] == -1 or ans[0] > cnt:
            ans[0] = cnt
        return
    
    tmp = y - x
    if v[index] - y == tmp:
        cal(y, v[index], index + 1, cnt, v, ans)
    elif v[index] + 1 - y == tmp:
        cal(y, v[index] + 1, index + 1, cnt + 1, v, ans)
    elif v[index] - 1 - y == tmp:
        cal(y, v[index] - 1, index + 1, cnt + 1, v, ans)
    else:
        return

def main():
    n = int(input())
    v = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        return

    ans = [-1]
    
    cal(v[0], v[1], 2, 0, v, ans)
    cal(v[0], v[1] + 1, 2, 1, v, ans)
    cal(v[0], v[1] - 1, 2, 1, v, ans)
    
    cal(v[0] + 1, v[1], 2, 1, v, ans)
    cal(v[0] + 1, v[1] + 1, 2, 2, v, ans)
    cal(v[0] + 1, v[1] - 1, 2, 2, v, ans)
    
    cal(v[0] - 1, v[1], 2, 1, v, ans)
    cal(v[0] - 1, v[1] + 1, 2, 2, v, ans)
    cal(v[0] - 1, v[1] - 1, 2, 2, v, ans)
    
    print(ans[0])

if __name__ == "__main__":
    main()
