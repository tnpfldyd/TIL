import sys
from itertools import combinations

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        nums = list(map(int, line.split()))[1:]
        for comb in combinations(nums, 6):
            print(' '.join(map(str, comb)))
        print()

if __name__ == '__main__':
    main()