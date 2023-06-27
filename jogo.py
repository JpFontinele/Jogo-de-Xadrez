import pygame
import time
from modules.board import *
from modules.oponent import *

#Tela
pygame.display.set_caption("jogo de xadrez")
screen = pygame.display.set_mode((800, 500))
bg = pygame.image.load("assets/fundo/telaGame.png").convert()

board = Board()

#Rodada
turnIndicatorWhite = pygame.image.load("assets/pecas/white_queen.png").convert_alpha()
turnIndicatorBlack = pygame.image.load("assets/pecas/black_queen.png").convert_alpha()


#Sprites
global allSpritesList, sprites
allSpritesList = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]
allSpritesList.add(sprites)

# desenho do sprite
allSpritesList.draw(screen)

# FPS
clock = pygame.time.Clock()

def tileSelected():
    x, y = pygame.mouse.get_pos()
    x = x // 60
    y = y // 60
    return (y, x)

# variaves de controle
running = True
pieceSelected = False
player = "white"
roundWhite = True

Rects = pygame.sprite.Group()
trans_table = dict()



# main loop
while running:

    #desenho da Tela
    screen.blit(bg, (0, 0))

    #Rodada das peças
    if roundWhite:
        screen.blit(turnIndicatorWhite, (700 - turnIndicatorWhite.get_width(), 150))
    else:
        screen.blit(turnIndicatorBlack, (700 - turnIndicatorBlack.get_width(), 150))
        

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Rodada das peças brancas
        if player == "white":
            roundWhite = True
            if event.type == pygame.MOUSEBUTTONDOWN and not pieceSelected:
                # Set the x, y positions of the mouse click
                x, y = event.pos
                clickedSprites = [ s for s in sprites if s.rect.collidepoint(event.pos)]
                if(len(clickedSprites) > 0) and clickedSprites[0].color == "white":
                    if not clickedSprites[0].highlighted:
                        clickedSprites[0].sethighlighted()

                    for s in sprites:  # allow only one highlighted
                        if s != clickedSprites[0] and s.highlighted:
                            s.unsethighlighted()
                            Rects = set()

                    pieceMoves = clickedSprites[0].genLegalMoves(board)
                    pieceSelected = True

                    for move in pieceMoves:
                        movementRect = MovementRect(move[0], move[1], screen)
                        Rects.add(movementRect)

            elif event.type == pygame.MOUSEBUTTONDOWN and pieceSelected:
                tile = tileSelected()
                pieceSelected = False
                Rects = set()
                specialMovesRoque = specialMoveGen(board, "white")
                enPassant = checkEnPassant(board, clickedSprites[0], "white")

                if tile in pieceMoves:
                    oldx = clickedSprites[0].x
                    oldy = clickedSprites[0].y
                    dest = board.array[tile[0]][tile[1]]

                    piecePromotion = board.movePiece(
                        clickedSprites[0], tile[0], tile[1])

                    if piecePromotion:
                        allSpritesList.add(piecePromotion[0])
                        sprites.append(piecePromotion[0])
                        allSpritesList.remove(piecePromotion[1])
                        sprites.remove(piecePromotion[1])

                    if dest:
                        allSpritesList.remove(dest)
                        sprites.remove(dest)

                    attacked = generatePossibleMoves(board, "black", True)

                    if (board.whiteKing.y, board.whiteKing.x) not in attacked:
                        selected = False
                        player = "black"

                        if dest:
                            board.score -= board.pieceValues[type(dest)]

                    else:  # THIS MOVE IS IN CHECK, we have to reverse it
                        board.movePiece(clickedSprites[0], oldy, oldx)
                        if type(clickedSprites[0]) == King or type(clickedSprites[0]) == Rook:
                            clickedSprites[0].moved = False
                        board.array[tile[0]][tile[1]] = dest
                        if dest:  # if dest not None
                            allSpritesList.add(dest)
                            sprites.append(dest)
                        if piecePromotion:
                            allSpritesList.add(piecePromotion[1])
                            sprites.append(piecePromotion[1])
                        clickedSprites[0].sethighlighted()

                        # different sidemenus depend on whether or not you're
                        # currently in check
                        if checkWhite:
                            #pygame.display.update()
                            pygame.time.wait(1000)
                        else:
                            #pygame.display.update()
                            pygame.time.wait(1000)


                elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                    clickedSprites[0].unsethighlighted()
                    selected = False

                elif enPassant:
                    if(tile[0] == clickedSprites[0].y-1 and tile[1] == clickedSprites[0].x+1 or tile[0] == clickedSprites[0].y-1 and tile[1] == clickedSprites[0].x-1):
                        special = "EP"
                        board.movePiece(
                            clickedSprites[0], tile[0], tile[1], special)

                        selected = False
                        player = "black"

                elif specialMovesRoque and tile in specialMovesRoque:
                    special = specialMovesRoque[tile]
                    if (special == "CR" or special == "CL") and type(clickedSprites[0]) == King:
                        board.movePiece(
                            clickedSprites[0], tile[0], tile[1], special)
                        selected = False
                        player = "black"

                    else:
                        pygame.display.update()
                        pygame.time.wait(1000)

                elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                    clickedSprites[0].unsethighlighted()
                    selected = False


        elif player == 'black':
            roundWhite = False
            value, move = minimax(board, 3, float(
                "-inf"), float("inf"), True, trans_table)

            if value == float("-inf") and move == 0:
                print("AI checkmate")
                player = 'white'
                running = False

            else:
                start = move[0]
                end = move[1]
                piece = board.array[start[0]][start[1]]
                dest = board.array[end[0]][end[1]]

                piecePromotion = board.movePiece(piece, end[0], end[1])
                if piecePromotion:
                    allSpritesList.add(piecePromotion[0])
                    sprites.append(piecePromotion[0])
                    allSpritesList.remove(piecePromotion[1])
                    sprites.remove(piecePromotion[1])

                if dest:
                    allSpritesList.remove(dest)
                    sprites.remove(dest)
                    board.score += board.pieceValues[type(dest)]

                player = 'white'
                attacked = generatePossibleMoves(board, "black", True)
                if (board.whiteKing.y, board.whiteKing.x) in attacked:
                    checkWhite = True
                else:
                    checkWhite = False

            if value == float("inf"):
                print("Player checkmate")
                running = False
                player = 'AI'
    

    allSpritesList = pygame.sprite.Group()
    sprites = [piece for row in board.array for piece in row if piece]
    allSpritesList.add(sprites)
    allSpritesList.add(Rects)

    # draw the sprites
    allSpritesList.draw(screen)
    allSpritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)