from collections import deque

n, k = map(int, input().split())


# 움직일 수 있는 최대 좌표는 100000
max_coordinate = 100001
# 해당 위치에 도착했을 때 시간을 표시하는 리스트
# 시작하지 않아서 0으로 시작
visited = [-1] * (max_coordinate + 1)

result = 0
start = 0
cnt = 0
# bfs 함수 정의
def bfs(n):
    global cnt, result
    # deque에 담아주고 넣어준다.
    queue = deque()
    queue.append((n, start))
    # queue가 있을때까지 돌아주기
    while queue:
        # 그 빼준값이 동생의 위치와 일치하면 종료
        now, time = queue.popleft()
        if now == k:
            cnt += 1
            result = time

        way = [now - 1, now + 1, now * 2]

        for w in way:
            if w >= 0 and w < max_coordinate:
                if visited[w] == -1 or visited[w] >= visited[now] + 1:
                    visited[w] = visited[now] + 1
                    queue.append((w, time + 1))


ans = bfs(n)
print(result)
print(cnt)