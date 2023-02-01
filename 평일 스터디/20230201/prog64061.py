def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for move in moves:
        move -= 1
        for i in range(N):
            if board[i][move]:
                stack.append(board[i][move])
                if len(stack) > 1 and stack[-1] == stack[-2]:
                    stack.pop(); stack.pop()
                    answer += 2
                board[i][move] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))