def main():
    print(solution())

def solution():
    input_str = input()
    return solution_helper(input_str)

def solution_helper(input_str):
    length = len(input_str)
    count1 = count_pattern(input_str, "KSA")
    count2 = count_pattern(input_str, "SAK")
    if count2 == length:
        count2 -= 1
    count3 = count_pattern(input_str, "AKS")
    if count3 >= length - 1:
        count3 = length - 2
    max_count = max(count1, count2, count3)
    answer = 2 * (length - max_count)
    return answer

def count_pattern(s, pattern):
    index = 0
    count = 0
    for char in s:
        if char == pattern[index]:
            index += 1
            count += 1
            if index == len(pattern):
                index = 0
    return count

if __name__ == "__main__":
    main()
