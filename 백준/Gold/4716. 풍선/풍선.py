import sys
input = sys.stdin.readline

def calculate_max_profit():
    while True:
        n, a, b = map(int, input().split())
        if n == a == b == 0:
            break
        
        arr = sorted(
            [list(map(int, input().split())) for _ in range(n)],
            key=lambda x: -abs(x[1] - x[2])
        )
        
        answer = 0
        
        for k, x, y in arr:
            if x <= y:
                val = min(k, a)
            else:
                val = k - min(k, b)
            
            answer += val * x + (k - val) * y
            a -= val
            b -= k - val
        
        print(answer)

if __name__ == "__main__":
    calculate_max_profit()