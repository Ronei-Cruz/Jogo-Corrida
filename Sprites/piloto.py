from pygame.locals import *
import pygame
import sys
from random import randint
import os

pygame.init()

largura = 420
altura = 600

pasta_principal = os.path.dirname(__file__)
pasta_imagens = os.path.join(pasta_principal, 'carros')
pasta_background = os.path.join(pasta_principal, 'background_pista')
pasta_sons = os.path.join(pasta_principal, 'Loops_Veiculos')

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Corrida')

carros_sheet = pygame.image.load(os.path.join(pasta_imagens, 'carros.png')).convert_alpha()
fundo1 = pygame.image.load(os.path.join(pasta_background, 'pista2.png')).convert_alpha()     # trago a imagem de fundo para o jogo

fundo2 = pygame.transform.scale(fundo1, (largura,altura)).convert()         # redimensionar imagem com o tamanho da tela
y = 600

som_colisao = pygame.mixer.Sound(os.path.join(pasta_sons, 'ColisoesFortes/batidaForte3.wav'))
som_colisao.set_volume(1)
colidiu = False

pontos = 0

def exibir_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

class Piloto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.andando = pygame.mixer.Sound(os.path.join(pasta_sons, 'Formula1/Andando.wav'))
        self.andando.set_volume(0.5)
        self.img_pilotos = []
        for i in range(4):
            imagem = carros_sheet.subsurface((i * 64,0),(64,64))
            self.img_pilotos.append(imagem)

        self.index_lista = 0
        self.image = self.img_pilotos[self.index_lista]
        self.rect = self.image.get_rect()                    # pega o retangulo em volta da imagem
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (240, 500)                       # redireciona a imagem na posição x e y
        self.desviar_e = False
        self.desviar_d = True

    def esquerda(self):
        self.desviar_e = True

    def direita(self):
        self.desviar_d = False
    

    def update(self):
        self.andando.play()
        if self.desviar_e == True:
            if self.rect.x <= 180:
                self.desviar_e = False
            self.rect.x -= 30
        elif self.desviar_d == False:
            if self.rect.x <= 280:
                self.desviar_d = True
            self.rect.x += 60
        
        if self.index_lista > 3:
            self.index_lista = 0
        self.index_lista += 0.5
        self.image = self.img_pilotos[int(self.index_lista)]

class Vermelho(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_vermelho = []
        
        i = 4
        # pegar a imagem dentro da posição x até y
        for i in range(7):
            vermelho = carros_sheet.subsurface((i * 64, 0),(64,64))
            self.img_vermelho.append(vermelho)
    
        self.index_lista = 4
        self.image = self.img_vermelho[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (240, 0)

    def update(self):
        if self.rect.y > 600:
            self.rect.y = 0
        self.rect.y += 10

        if self.index_lista > 6:
            self.index_lista = 4
        self.index_lista += 0.25
        self.image = self.img_vermelho[int(self.index_lista)]

class Verde(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_verde = []

        i = 7

        for i in range(10):
            verde = carros_sheet.subsurface((i * 64, 0), (64, 64))
            self.img_verde.append(verde)

        self.index_lista = 7
        self.image = self.img_verde[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (240,300)

    def update(self):
        if self.rect.y > 600:
            self.rect.y = 0
        self.rect.y += 10

        if self.index_lista > 9:
            self.index_lista = 7
        self.index_lista += 0.25
        self.image =self.img_verde[int(self.index_lista)]

class Azul(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_azul = []

        i = 7

        for i in range(13):
            azul = carros_sheet.subsurface((i * 64, 0), (64, 64))
            self.img_azul.append(azul)

        self.index_lista = 10
        self.image = self.img_azul[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (180,150)

    def update(self):
        if self.rect.y > 600:
            self.rect.y = 0
        self.rect.y += 15

        if self.index_lista > 12:
            self.index_lista = 10
        self.index_lista += 0.25
        self.image =self.img_azul[int(self.index_lista)]

todos_pilotos = pygame.sprite.Group()
piloto = Piloto()
carro_vermelho = Vermelho()
carro_verde = Verde()
carro_azul = Azul()
todos_pilotos.add(piloto)
todos_pilotos.add(carro_vermelho, carro_verde, carro_azul)

obstaculos_carros = pygame.sprite.Group()
obstaculos_carros.add(carro_verde, carro_azul, carro_vermelho)

relogio = pygame.time.Clock()

while True:
    relogio.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                piloto.esquerda()
            elif event.key == K_d:
                piloto.direita()

    # Posição do background relativa em y para que ele se repita em um loop
    rel_y = y % fundo2.get_rect().height
    tela.blit(fundo2, (0,rel_y - fundo2.get_rect().height))
    if y > 0:
        tela.blit(fundo2,(0, rel_y))
    y += 5
    guad1 = pygame.draw.line(tela,(220,220,220), (120, 0), (120, 600), 4)
    guad2 = pygame.draw.line(tela,(220,220,220), (300, 0), (300, 600), 4)

    colisoes = pygame.sprite.spritecollide(piloto, obstaculos_carros, False, pygame.sprite.collide_mask)
    todos_pilotos.draw(tela)

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True
    elif colidiu == True:
        pass
    else:
        pontos += 1
        todos_pilotos.update()
        texto_pontos = exibir_mensagem(pontos, 40, (0,0,0))
    
    tela.blit(texto_pontos, (350,50))

    pygame.display.flip()