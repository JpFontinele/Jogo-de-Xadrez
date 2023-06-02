from modules.board import *

def checkCastling(board,c,side):
    castleLeft = False
    castleRight = False

    if c == "white":
        king = board.whiteKing
        leftRook = board.whiteRookLeft
        rightRook =  board.whiteRookRight
        attacked = generatePossibleMoves(board, "black", True)
        row = 7
    elif c == "b":
        king = board.blackKing
        leftRook = board.blackRookLeft
        rightRook =  board.blackRookRight
        attacked = generatePossibleMoves(board, "w", True)
        row = 0

    squares = set()

    if king.moved == False:
        if board.array[row][0] == leftRook and leftRook.moved == False:
            squares = {(row,1),(row,2),(row,3)}
            if not board.array[row][1] and not board.array[row][2] and not board.array[row][3]:
                if not attacked.intersection(squares):
                    castleLeft = True
        
        if board.array[row][7] == rightRook and rightRook.moved == False:
            squares = {(row,6),(row,5)}
            if not board.array[row][6] and not board.array[row][5]:
                if not attacked.intersection(squares):
                    castleRight = True

    if side == "r":
        return castleRight
    elif side == "l":
        return castleLeft

def specialMoveGen(board,color,moves = None):
    if moves == None:
        moves = dict()
    if color == "white":
        x = 7
    elif color == "black":
        x = 0
    rightCastle = checkCastling(board,color,"r")
    leftCastle = checkCastling(board,color,"l")

    if rightCastle:
        moves[(x,6)] = "CR"
    if leftCastle:
        moves[(x,2)] = "CL"

    return moves

def checkEnPassant(board,piece,color):
    if (type(piece) == Pawn):
        if(color == "white" and piece.y == 3):
            if(type(board.array[3][piece.x+1]) == Pawn and board.array[3][piece.x+1].color == "black" or type(board.array[3][piece.x-1]) == Pawn and board.array[3][piece.x-1].color == "black"):
                return 1
        elif(color == "black" and piece.y == 4):
            if(type(board.array[4][piece.x+1]) == Pawn and board.array[4][piece.x+1].color == "white" or type(board.array[4][piece.x-1]) == Pawn and board.array[4][piece.x-1].color == "white"):
                return 1
    return 0

def matrixToTuple(array, arrayEmpty):
    for i in range(8):
        arrayEmpty[i] = tuple(array[i])
    return tuple(arrayEmpty)


def generatePossibleMoves(board, color, attc=False):
    if attc:
        moves = set()
    else:
        moves = dict()

    for j in range(8):
        for i in range(8):
            piece = board.array[i][j]
            if piece != None and piece.color == color:
                legalMoves = piece.genLegalMoves(board)
                if legalMoves and not attc:
                    moves[(i, j)] = legalMoves
                elif legalMoves and attc:
                    moves = moves.union(legalMoves)

    return moves


def minimax(board, depth, alpha, beta, maximizing, lastMove):
    boardTuple = matrixToTuple(board.array, board.empty)

    if boardTuple in lastMove and depth != 3:
        return lastMove[boardTuple], 0

    if depth == 0:
        lastMove[boardTuple] = board.score
        return board.score, 0

    if maximizing:
        bestValue = float("-inf")
        blackMoves = generatePossibleMoves(board, "black")

        for start, moveSet in blackMoves.items():
            for end in moveSet:

                piece = board.array[start[0]][start[1]]
                dest = board.array[end[0]][end[1]]

                pawnPromotion = board.movePiece(piece, end[0], end[1], False)

                attacked = generatePossibleMoves(board, "white", True)
                if (board.blackKing.y, board.blackKing.x) in attacked:
                    board.movePiece(piece, start[0], start[1], False, True)
                    board.array[end[0]][end[1]] = dest
                    if pawnPromotion:
                        board.score -= 9
                    continue

                if dest != None:
                    board.score += board.pieceValues[type(dest)]

                v, __ = minimax(board, depth - 1, alpha, beta, False, lastMove)

                board.movePiece(piece, start[0], start[1], False, True)
                board.array[end[0]][end[1]] = dest

                if pawnPromotion:
                    board.score -= 9

                if dest != None:
                    board.score -= board.pieceValues[type(dest)]

                if v >= bestValue:
                    move = (start, (end[0], end[1]))

                bestValue = max(bestValue, v)
                alpha = max(alpha, bestValue)

                if beta <= alpha:
                    return bestValue, move
        try:
            return bestValue, move
        except:
            return bestValue, 0

    else:
        bestValue = float("inf")
        whiteMoves = generatePossibleMoves(board, "white")

        for start, moveSet in whiteMoves.items():
            for end in moveSet:

                piece = board.array[start[0]][start[1]]
                dest = board.array[end[0]][end[1]]
                pawnPromotion = board.movePiece(piece, end[0], end[1], False)

                attacked = generatePossibleMoves(board, "black", True)
                if (board.whiteKing.y, board.whiteKing.x) in attacked:
                    board.movePiece(piece, start[0], start[1], False, True)
                    board.array[end[0]][end[1]] = dest
                    if pawnPromotion:
                        board.score += 9
                    continue

                if dest != None:
                    board.score -= board.pieceValues[type(dest)]

                v, __ = minimax(board, depth - 1, alpha, beta, True, lastMove)

                bestValue = min(v, bestValue)
                beta = min(beta, bestValue)

                board.movePiece(piece, start[0], start[1], False, True)
                board.array[end[0]][end[1]] = dest
                if pawnPromotion:
                    board.score += 9
                if dest != None:
                    board.score += board.pieceValues[type(dest)]

                if beta <= alpha:
                    return bestValue, 0

        return bestValue, 0
