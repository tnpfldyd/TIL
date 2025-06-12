def find_max_budget(requests, total_budget):
    left, right = 0, max(requests)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        allocated = sum(min(req, mid) for req in requests)

        if allocated <= total_budget:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

N = int(input())
requests = list(map(int, input().split()))
M = int(input())

print(find_max_budget(requests, M))