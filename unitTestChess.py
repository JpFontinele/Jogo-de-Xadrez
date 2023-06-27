""" Arquivo para testar as funçoes de cada modulo """
# importando todos os modulos menos a main
import unittest
import pygame
from modules.board import *
from modules.oponent import *
from modules.pieces import *


class Test(unittest.TestCase):
    """ Classe teste na qual possui todas as funçoes de testagem do jogo """
    # iniciando o pygame para poder iniciar os testes
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # criando tela
    board = Board()  # dando init no tabuleiro

    def test_get_board(self):
        """ Testando se o tabuleiro criado é realmente um lista ou não """
        self.assertIsInstance(self.board.getBoard(), list)

    def test_move_piece(self):
        """ Verifica se a função retorna o que se é esperado da função de movimento """
        # cria uma peça do tipo pião na matriz com posição [1,1]
        piece = Pawn("white", 1, 1)
        # checando se o retorno da função é realmente uma tupla
        self.assertIsInstance(self.board.movePiece(piece, 0, 0), tuple)

    def test_piece_promotion(self):
        """ Testa as possibilidades de promoção da peça """
        # cria uma peça do tipo pião na matriz com posição [1,1]
        piece = Pawn("white", 1, 1)
        # checando se a peça quando movida para uma posição com y = 1 ela
        # retorna True
        self.assertTrue(checkPiecePromotion(piece, 0))
        # checando se a peça quando movida para uma posição com y = 2 ela
        # retorna False
        self.assertFalse(checkPiecePromotion(piece, 2))

    def test_capture_tile(self):
        """ Verifica se peça pode tomar a posição """
        # checa se peça branca pode ir para posição de uma peça preta
        self.assertTrue(captureTile("white", 0, 0, self.board))
        # checa se quadrado está vazio
        self.assertFalse(captureTile("white", 3, 3, self.board))
        # checa se peça branca pode ir para posição de uma peça branca
        self.assertFalse(captureTile("white", 7, 7, self.board))

    def test_move_check(self):
        """ Checa se movimentação é valida ou não """
        # checa movimentação invalida
        self.assertFalse(moveCheck("white", 8, 8, self.board))
        # checa movimentação invalida
        self.assertFalse(moveCheck("white", -1, -1, self.board))
        # checa movimentação para um campo vazio
        self.assertTrue(moveCheck("white", 3, 3, self.board))
        # checa movimentação para um campo com peça rival
        self.assertTrue(moveCheck("white", 0, 0, self.board))
        # checa movimentação para um campo com peça da mesma cor
        self.assertFalse(moveCheck("white", 6, 6, self.board))

    def test_line_attack(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # cria uma peça do tipo torre na matriz com posição [3,3]
        piece = Rook("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.lineAttackMoves(self.board), set)

    def test_diagonal_attack(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # cria uma peça do tipo torre na matriz com posição [3,3]
        piece = Bishop("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.diagonalAttackMoves(self.board), set)

    def test_all_gen_legal_moves(self):
        """ Verifica se é retornado a tipo certo de variavel para todas as peças """
        # cria uma peça do tipo pião na matriz com posição [3,3]
        piece = Pawn("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)
        # cria uma peça do tipo bispo na matriz com posição [3,3]
        piece = Bishop("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)
        # cria uma peça do tipo cavalo na matriz com posição [3,3]
        piece = Knight("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)
        # cria uma peça do tipo torre na matriz com posição [3,3]
        piece = Rook("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)
        # cria uma peça do tipo rei na matriz com posição [3,3]
        piece = King("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)
        # cria uma peça do tipo rainha na matriz com posição [3,3]
        piece = Queen("white", 3, 3)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(piece.genLegalMoves(self.board), set)

    def test_gen_possible_moves(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # checando se o retorno da função é realmente um dicionario
        self.assertIsInstance(generatePossibleMoves(self.board, "white"), dict)
        # checando se o retorno da função é realmente um set
        self.assertIsInstance(generatePossibleMoves(
            self.board, "white", True), set)

    def test_matrix_2_tuple(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # checando se o retorno da função é realmente uma tupla
        self.assertIsInstance(matrixToTuple(
            self.board.array, self.board.empty), tuple)

    def test_minimax(self):
        """ Verifica se é retornado a tipo certo de variavel """
        last = dict()
        # checando se o retorno da função é realmente uma tupla
        self.assertIsInstance(minimax(self.board, 3, float(
            '-inf'), float('inf'), True, last), tuple)
        # checando se o retorno da função é realmente uma tupla
        self.assertIsInstance(minimax(self.board, 0, float(
            '-inf'), float('inf'), True, last), tuple)

    def test_enpassant(self):
        """ Verifica se é retornado a tipo certo de variavel """
        piece = Knight("white", 3, 3)
        # checando se o retorno da função é realmente um inteiro
        self.assertIsInstance(checkEnPassant(self.board, piece, "white"), int)

    def test_special_move_gen(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # checando se o retorno da função é realmente um dicionario
        self.assertIsInstance(specialMoveGen(self.board,"white"), dict)

    def test_check_castling(self):
        """ Verifica se é retornado a tipo certo de variavel """
        # checando se o retorno da função é realmente um bool
        self.assertIsInstance(checkCastling(self.board,"white","r"), bool)

    def test_special_move(self):
        """ Verifica se é executado sem erros"""
        piece = Knight("white", 3, 3)
        # checando se a funcao realmente não tem retorno
        self.assertIsInstance(self.board.specialMove(piece,0,0,"CR"), type(None))


if __name__ == '__main__':
    unittest.main()
