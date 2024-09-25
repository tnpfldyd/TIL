def main():
    string_a = input().strip()
    string_b = input().strip()

    index_b = len(string_b) - 1
    operation_count = 0

    for i in range(len(string_a) - 1, -1, -1):
        if string_a[i] == string_b[index_b]:
            index_b -= 1
        else:
            operation_count += 1

    sorted_a = sorted(string_a)
    sorted_b = sorted(string_b)

    if sorted_a == sorted_b:
        print(operation_count)
    else:
        print(-1)

if __name__ == "__main__":
    main()