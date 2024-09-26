import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    if m < 3:
        print(0)
        return

    three_gram = []
    five_gram = []

    for _ in range(n):
        t, s = map(int, input().split())
        if t == 3:
            three_gram.append(s)
        else:
            five_gram.append(s)

    three_gram.sort(reverse=True)
    five_gram.sort(reverse=True)

    three_sum = [0] * (len(three_gram) + 1)
    five_sum = [0] * (len(five_gram) + 1)

    for i in range(1, len(three_gram) + 1):
        three_sum[i] = three_gram[i-1] + three_sum[i-1]

    for i in range(1, len(five_gram) + 1):
        five_sum[i] = five_gram[i-1] + five_sum[i-1]

    five_size = len(five_gram)
    t_idx = min(len(three_gram), m // 3)
    max_sweetness = 0

    while t_idx >= 0:
        f_idx = min((m - 3 * t_idx) // 5, five_size)
        current_sweetness = three_sum[t_idx] + five_sum[f_idx]
        max_sweetness = max(max_sweetness, current_sweetness)
        t_idx -= 1

    print(max_sweetness)

if __name__ == "__main__":
    main()