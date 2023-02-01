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