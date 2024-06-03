import math

def main():
    a, b, c = map(float, input().split())
    cur = 0

    while abs(a * cur + b * math.sin(cur) - c) > 1e-9:
        nxt = cur - (a * cur + b * math.sin(cur) - c) / (a + b * math.cos(cur))
        cur = nxt

    print(f"{cur:.9f}")

if __name__ == "__main__":
    main()
