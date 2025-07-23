def solve_inequality(k, operators):
    used = [False] * 10
    result = []
    all_results = []
    
    def is_valid():
        for i in range(len(result) - 1):
            if i < len(operators):
                if operators[i] == '<' and result[i] >= result[i + 1]:
                    return False
                elif operators[i] == '>' and result[i] <= result[i + 1]:
                    return False
        return True
    
    def backtrack(pos):
        if pos == k + 1:
            if is_valid():
                all_results.append(result[:])
            return
        
        for num in range(10):
            if not used[num]:
                used[num] = True
                result.append(num)
                
                if is_valid():
                    backtrack(pos + 1)
                
                result.pop()
                used[num] = False
    
    backtrack(0)
    
    string_results = []
    for nums in all_results:
        string_results.append(''.join(map(str, nums)))
    
    max_result = max(string_results)
    min_result = min(string_results)
    
    return max_result, min_result

k = int(input().strip())
operators = input().strip().split()

max_val, min_val = solve_inequality(k, operators)

print(max_val)
print(min_val)