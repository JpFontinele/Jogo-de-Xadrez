import pygame
from modules.board import *

# Tela
pygame.display.set_caption("Jogo de Xadrez")
screen = pygame.display.set_mode((800, 500))
bg = pygame.image.load("assets/fundo/telaGame.png").convert()

board = Board()

# Rodada
turnIndicatorWhite = pygame.image.load("assets/pecas/white_queen.png").convert_alpha()
turnIndicatorBlack = pygame.image.load("assets/pecas/black_queen.png").convert_alpha()

# Sprites
allSpritesList = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]
allSpritesList.add(sprites)

# Desenho do sprite
allSpritesList.draw(screen)

# FPS
clock = pygame.time.Clock()

def tileSelected():
    x, y = pygame.mouse.get_pos()
    x = x // 60
    y = y // 60
    return (y, x)

# Variáveis de controle
running = True
pieceSelected = False
player = "white"

Rects = pygame.sprite.Group()
trans_table = dict()

# Main loop
while running:

    # Desenho da tela
    screen.blit(bg, (0, 0))

    # Rodada das peças
    if player == "white":
        screen.blit(turnIndicatorWhite, (700 - turnIndicatorWhite.get_width(), 150))
    else:
        screen.blit(turnIndicatorBlack, (700 - turnIndicatorBlack.get_width(), 150))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not pieceSelected:
            # Set the x, y positions of the mouse click
            x, y = event.pos
            clickedSprites = [s for s in sprites if s.rect.collidepoint(event.pos)]
            if len(clickedSprites) > 0 and clickedSprites[0].color == player:
                if not clickedSprites[0].highlighted:
                    clickedSprites[0].sethighlighted()

                for s in sprites:
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

            if tile in pieceMoves:
                dest = board.array[tile[0]][tile[1]]

                board.movePiece(clickedSprites[0], tile[0], tile[1])

                if dest:
                    allSpritesList.remove(dest)
                    sprites.remove(dest)

                player = "black" if player == "white" else "white"

            elif (clickedSprites[0].y, clickedSprites[0].x) == tile:
                clickedSprites[0].unsethighlighted()

    allSpritesList = pygame.sprite.Group()
    sprites = [piece for row in board.array for piece in row if piece]
    allSpritesList.add(sprites)
    allSpritesList.add(Rects)

    # Desenhe os sprites
    allSpritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)