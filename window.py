import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.mixer.music.load('BoxCat Games - Inspiration.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

som_de_pontuação = pygame.mixer.Sound('smw_coin.wav')
som_de_pontuação.set_volume(1)

largura = 640
altura = 480

xBola = largura/2
yBola = altura/2
velocidadeDaBolay = 3
velocidadeDaBolax = 3
raioDaBola = 10

fonte = pygame.font.SysFont('arial', 30, True, True)
pontosAzul = 0
pontosVermelho = 0

yJogador1 = altura/2 - 5 * raioDaBola/2
velocidadeJogador = 8
yjogador2 = altura/2 - 5 * raioDaBola/2


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('PRONG')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    azul = f'AZUL: {pontosAzul}'
    vermelho = f'VERMELHO: {pontosVermelho}'

    azul_formatado = fonte.render(azul, True, (0, 0, 255))
    vermelho_formatado = fonte.render(vermelho, True, (255, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_w:
                yJogador1 -= 30
            elif event.key == K_s:
                yJogador1 += 30
            if event.key == K_UP:
                yjogador2 -= 30
            elif event.key == K_DOWN:
                yjogador2 += 30'''
    if pygame.key.get_pressed()[K_w]:
        yJogador1 -= velocidadeJogador
    elif pygame.key.get_pressed()[K_s]:
        yJogador1 += velocidadeJogador
    if pygame.key.get_pressed()[K_UP]:
        yjogador2 -= velocidadeJogador
    elif pygame.key.get_pressed()[K_DOWN]:
        yjogador2 += velocidadeJogador
    
    
    pygame.draw.circle(tela, (255, 255, 0), (xBola, yBola), raioDaBola)
    pygame.draw.rect(tela, (0, 255 , 255), (5, yJogador1, raioDaBola, 5 * raioDaBola))
    pygame.draw.rect(tela, (255, 0 ,0), (largura - raioDaBola - 5, yjogador2, raioDaBola, 5 * raioDaBola))

    yBola -= velocidadeDaBolay
    xBola -= velocidadeDaBolax

    if xBola + raioDaBola > largura - raioDaBola - 5 and yBola + raioDaBola > yjogador2 and yBola - raioDaBola < yjogador2 + 5 * raioDaBola:
        velocidadeDaBolax = -velocidadeDaBolax
        velocidadeDaBolax += 1
        velocidadeJogador += 0.2
    
    if xBola + raioDaBola < 35 and yBola + raioDaBola > yJogador1 and yBola - raioDaBola < yJogador1 + 5 * raioDaBola:
        velocidadeDaBolax = -velocidadeDaBolax
        velocidadeDaBolax -= 1
        velocidadeJogador += 0.2
    
    if xBola + raioDaBola < 0:
        xBola = largura/2
        yBola = altura/2
        velocidadeDaBolax = 3
        velocidadeDaBolay = 3
        velocidadeJogador = 8
        pontosVermelho += 1
        som_de_pontuação.play()

    if xBola - raioDaBola > largura:
        xBola = largura/2
        yBola = altura/2
        velocidadeDaBolax = -3
        velocidadeDaBolay = -3
        velocidadeJogador = 8
        pontosAzul += 1
        som_de_pontuação.play()
    
    if yBola + raioDaBola > altura or yBola + raioDaBola < 22:
        velocidadeDaBolay = -velocidadeDaBolay
    
    if yJogador1 > altura:
        yJogador1 = 0 - 5 * raioDaBola
    elif yJogador1 + 5 * raioDaBola < 0:
        yJogador1 = altura
    
    if yjogador2 > altura:
        yjogador2 = 0 - 5 * raioDaBola
    elif yjogador2 + 5 * raioDaBola < 0:
        yjogador2 = altura

    tela.blit(azul_formatado, (50, 50))
    tela.blit(vermelho_formatado, (400, 50))
    pygame.display.update()
