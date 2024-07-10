
def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    N = int(input().strip())
    
    numbers = list(map(int, input().strip().split()))
    
    gcd_left_to_right = [0] * N
    gcd_right_to_left = [0] * N
    
    gcd_left_to_right[0] = numbers[0]
    gcd_right_to_left[N - 1] = numbers[-1]
    
    for i in range(1, N):
        previous_gcd = gcd_left_to_right[i - 1]
        gcd_left_to_right[i] = calculate_gcd(max(previous_gcd, numbers[i]), min(previous_gcd, numbers[i]))
    
    for i in range(N - 2, -1, -1):
        previous_gcd = gcd_right_to_left[i + 1]
        gcd_right_to_left[i] = calculate_gcd(max(previous_gcd, numbers[i]), min(previous_gcd, numbers[i]))
    
    max_gcd = -1
    excluded_number = -1
    
    for i in range(N):
        if i == 0:
            if max_gcd < gcd_right_to_left[1]:
                max_gcd = gcd_right_to_left[1]
                excluded_number = numbers[i]
        elif i == N - 1:
            if max_gcd < gcd_left_to_right[N - 2]:
                max_gcd = gcd_left_to_right[N - 2]
                excluded_number = numbers[i]
        else:
            current_gcd = calculate_gcd(gcd_left_to_right[i - 1], gcd_right_to_left[i + 1])
            if max_gcd < current_gcd:
                max_gcd = current_gcd
                excluded_number = numbers[i]
    
    if excluded_number % max_gcd == 0:
        print("-1")
    else:
        print(f"{max_gcd} {excluded_number}")

if __name__ == "__main__":
    main()
