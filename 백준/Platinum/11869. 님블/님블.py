from functools import reduce
def main():
    input()
    result = reduce(lambda x, y: x ^ y, list(map(int, input().split())), 0)
    print("koosaga" if result else "cubelover")

if __name__ == "__main__":
    main()