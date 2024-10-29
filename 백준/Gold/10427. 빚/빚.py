import sys
input = sys.stdin.readline

def get_int_list():
    return list(map(int, input().strip().split()))

def get_int():
    return int(input().strip())

def main():
    output = []
    for _ in range(get_int()):
        data = get_int_list()
        n = data[0]
        origin = sorted(data[1:])
        pre_sum = [0] * (len(origin) + 1)

        for i in range(1, len(pre_sum)):
            pre_sum[i] = pre_sum[i - 1] + origin[i - 1]

        answer = 0
        for m in range(2, n + 1):
            min_value = float('inf')
            for i in range(n - m + 1):
                min_value = min(min_value, origin[i + m - 1] * m - (pre_sum[i + m] - pre_sum[i]))
            answer += min_value

        output.append(answer)

    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()