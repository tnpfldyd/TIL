def min_joystick_moves(name):
    total_moves = 0
    min_side_moves = len(name) - 1

    for i, char in enumerate(name):
        total_moves += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next_non_a = i + 1
        while next_non_a < len(name) and name[next_non_a] == 'A':
            next_non_a += 1

        min_side_moves = min(min_side_moves, 
                             i + i + len(name) - next_non_a,
                             i + 2 * (len(name) - next_non_a))

    return total_moves + min_side_moves

def main():
    T = int(input())
    for _ in range(T):
        name = input().strip()
        print(min_joystick_moves(name))

if __name__ == "__main__":
    main()