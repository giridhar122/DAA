def minimax(board, depth, isMaximizing):
    score = evaluate(board)
    if score == 1:
        return score
    if score == -1:
        return score
    if isMovesLeft(board) == False:
        return 0
    if isMaximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ''
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ''
        return best