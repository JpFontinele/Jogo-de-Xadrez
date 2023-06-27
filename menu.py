import pygame
import sys

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
largura = 800
altura = 500

# Criar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Xadrez")

# Carregar imagem
imagem = pygame.image.load("assets/fundo/telaMenu.png")  # Substitua "imagem.png" pelo caminho para sua imagem

# Botão "Jogar"
botao_jogar = pygame.Rect(largura // 2 - 50, altura - 150, 100, 50)

# Botão "Jogar com um amigo"
botao_jogar_amigo = pygame.Rect(largura // 2 - 110, altura - 80, 220, 50)

# Loop principal do jogo
while True:
    # Tratar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if botao_jogar.collidepoint(event.pos):
                # Redirecionar para o jogo.py
                exec(open("jogo.py").read())
            elif botao_jogar_amigo.collidepoint(event.pos):
                # Redirecionar para o jogo com um amigo
                exec(open("jogo_amigo.py").read())  # Substitua "jogo_amigo.py" pelo arquivo que corresponde ao jogo com um amigo

    # Preencher a tela com a cor branca
    tela.fill(BRANCO)

    # Desenhar a imagem
    tela.blit(imagem, (0, 0))

    # Desenhar o botão "Jogar"
    pygame.draw.rect(tela, PRETO, botao_jogar)
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("Jogar", True, BRANCO)
    texto_rect = texto.get_rect(center=botao_jogar.center)
    tela.blit(texto, texto_rect)

    # Desenhar o botão "Jogar com um amigo"
    pygame.draw.rect(tela, PRETO, botao_jogar_amigo)
    texto_amigo = fonte.render("Jogar com um amigo", True, BRANCO)
    texto_amigo_rect = texto_amigo.get_rect(center=botao_jogar_amigo.center)
    tela.blit(texto_amigo, texto_amigo_rect)

    # Atualizar a tela
    pygame.display.flip()
