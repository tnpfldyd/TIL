import sys
from heapq import heappop, heappush
input = sys.stdin.readline 

N = int(input())
pq = [] 
answer = [0] * (N + 1) 
lecture = [list(map(int, input().split())) for _ in range(N)] 

lecture.sort(key=lambda x: (x[1], x[2])) 

room_num = 1 
heappush(pq, [lecture[0][2], room_num]) 
answer[lecture[0][0]] = room_num 

for i in range(1, N): 
    if pq[0][0] > lecture[i][1]: 
        room_num += 1 
        answer[lecture[i][0]] = room_num 
        heappush(pq, [lecture[i][2], room_num]) 
    else: 
        temp = heappop(pq) 
        answer[lecture[i][0]] = temp[1] 
        heappush(pq, [lecture[i][2], temp[1]]) 

print(len(pq)) 
for i in range(1, len(answer)): 
    print(answer[i]) 
