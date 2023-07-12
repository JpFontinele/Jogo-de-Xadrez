import pygame


def captureTile(pieceColor, y, x, board):
    piece = board.array[y][x]
    if piece == None:
        return False
    else:
        if piece.color != pieceColor:
            return True
        else:
            return False


def moveCheck(pieceColor, y, x, board):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    piece = board.array[y][x]
    if piece == None:
        return True
    else:
        if piece.color != pieceColor:
            return True
        else:
            return False


class MovementRect(pygame.sprite.Sprite):
    def __init__(self, y, x, display):
        super().__init__()
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 63, y * 63
        pygame.draw.rect(self.image, (0, 0, 66, 170), (0, 0, 60, 60))


class Piece(pygame.sprite.Sprite):
    def __init__(self, color, y, x):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 60, y * 60
        self.highlighted = False
        self.symbol = ""

    def sethighlighted(self):
        self.highlighted = True
        self.update()

    def unsethighlighted(self):
        self.highlighted = False
        self.update()

    def lineAttackMoves(self, board):
        moveSet = set()
        newX = self.x

        for i in (-1, 1):
            newY = self.y
            while(True):
                newY += i
                if moveCheck(self.color, newY, newX, board):
                    moveSet.add((newY, newX))
                    if captureTile(self.color, newY, newX, board):
                        break
                else:
                    break

        newY = self.y

        for i in (-1, 1):
            newX = self.x
            while(True):
                newX += i
                if moveCheck(self.color, newY, newX, board):
                    moveSet.add((newY, newX))
                    if captureTile(self.color, newY, newX, board):
                        break
                else:
                    break

        return moveSet

    def diagonalAttackMoves(self, board):
        moveSet = set()

        increments = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
        for offset in increments:
            newX = self.x
            newY = self.y
            while (True):
                newX += offset[0]
                newY += offset[1]
                if moveCheck(self.color, newY, newX, board):
                    moveSet.add((newY, newX))
                    if captureTile(self.color, newY, newX, board):
                        break
                else:
                    break
        return moveSet


class Pawn(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.symbol = "P"
        self.sprite = pygame.image.load("assets/pecas/{}_pawn.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.image.blit(self.sprite, (5, 5))

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}Pawn.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_pawn.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):
        moveSet = set()

        incr = {"white": -1, "black": 1}
        offsets = [-1, 1]
        c = self.color

        newY = self.y + incr[c]
        if newY >= 0 and newY < 8 and board.array[newY][self.x] == None:
            moveSet.add((newY, self.x))

            if (self.y == 1 and c == "black") or (self.y == 6 and c == "white"):
                newY += incr[c]
                if newY >= 0 and newY < 8 and board.array[newY][self.x] == None:
                    moveSet.add((newY, self.x))

        for diff in offsets:
            newX = self.x + diff
            newY = self.y + incr[c]

            if not moveCheck(c, newY, newX, board) or not captureTile(c, newY, newX, board):
                continue

            else:
                moveSet.add((newY, newX))

        return moveSet


class Rook(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load("assets/pecas/{}_rook.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "R"
        self.image.blit(self.sprite, (5, 5))
        self.moved = False

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}Rook.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_rook.png".format(self.color))
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):

        return self.lineAttackMoves(board)


class Bishop(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "assets/pecas/{}_bishop.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "Black"
        self.image.blit(self.sprite, (5, 5))

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}Bishop.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_bishop.png".format(self.color))
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):

        return self.diagonalAttackMoves(board)


class Knight(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "assets/pecas/{}_knight.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "N"
        self.image.blit(self.sprite, (5, 5))

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}Knight.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_knight.png".format(self.color))
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):
        moveSet = set()
        offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]

        for offset in offsets:
            newX = self.x + offset[0]
            newY = self.y + offset[1]

            if moveCheck(self.color, newY, newX, board):
                moveSet.add((newY, newX))

        return moveSet


class King(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load("assets/pecas/{}_king.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "K"
        self.image.blit(self.sprite, (5, 5))
        self.moved = False

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}King.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_king.png".format(self.color))
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):
        moveSet = set()
        offsets = [(1, 1), (-1, -1), (1, -1), (-1, 1),
                   (0, 1), (1, 0), (-1, 0), (0, -1)]

        for offset in offsets:
            newX = self.x + offset[0]
            newY = self.y + offset[1]

            if moveCheck(self.color, newY, newX, board):
                moveSet.add((newY, newX))

        return moveSet


class Queen(Piece):
    def __init__(self, color, y, x):
        super().__init__(color, y, x)
        self.sprite = pygame.image.load(
            "assets/pecas/{}_queen.png".format(self.color))
        self.sprite = pygame.transform.scale(self.sprite, (50, 50))
        self.symbol = "Q"
        self.image.blit(self.sprite, (5, 5))

    def update(self):
        if self.highlighted:
            self.sprite = pygame.image.load(
                "assets/pecas/highlighted{}Queen.png".format(self.color)).convert_alpha()
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))
        else:
            self.sprite = pygame.image.load(
                "assets/pecas/{}_queen.png".format(self.color))
            self.sprite = pygame.transform.scale(self.sprite, (50, 50))
            self.image.blit(self.sprite, (5, 5))

    def genLegalMoves(self, board):

        moveSet1 = self.lineAttackMoves(board)
        moveSet2 = self.diagonalAttackMoves(board)

        return moveSet1.union(moveSet2)
