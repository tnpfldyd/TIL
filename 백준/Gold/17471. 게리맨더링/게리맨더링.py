import sys
import itertools
import collections

def bfs(same_group):
    start_node = same_group[0]
    queue = collections.deque([start_node])
    visited = set([start_node])
    total_population = 0
    
    while queue:
        current_node = queue.popleft()
        total_population += population[current_node]
        
        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor in same_group:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return total_population, len(visited)

n = int(sys.stdin.readline().strip())
population = list(map(int, input().split()))
graph = collections.defaultdict(list)
INF = sys.maxsize
minimum_difference = INF

for i in range(n):
    _, *adjacent_nodes = map(int, input().split())
    for node in adjacent_nodes:
        graph[i].append(node - 1)

for i in range(1, n // 2 + 1):
    combinations = list(itertools.combinations(range(n), i))
    for combination in combinations:
        population_sum1, visited_count1 = bfs(combination)
        population_sum2, visited_count2 = bfs([node for node in range(n) if node not in combination])
        
        if visited_count1 + visited_count2 == n:
            minimum_difference = min(minimum_difference, abs(population_sum1 - population_sum2))

print(minimum_difference if minimum_difference != INF else -1)
