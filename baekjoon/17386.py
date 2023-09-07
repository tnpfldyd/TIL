class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    temp = (A.x * B.y) + (B.x * C.y) + (C.x * A.y)
    temp -= (A.x * C.y) + (B.x * A.y) + (C.x * B.y)

    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    else:
        return -1

def check(A, B, C, D):
    ans1 = ccw(A, B, C) * ccw(A, B, D)
    ans2 = ccw(C, D, A) * ccw(C, D, B)

    return ans1 < 0 and ans2 < 0

def main():
    arr = [list(map(int, input().split())) for _ in range(2)]
    A, B = Coordinate(arr[0][0], arr[0][1]), Coordinate(arr[0][2], arr[0][3])
    C, D = Coordinate(arr[1][0], arr[1][1]), Coordinate(arr[1][2], arr[1][3])
    if check(A, B, C, D):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()