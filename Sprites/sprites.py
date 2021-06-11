import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 430

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_1.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_2.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_3.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_4.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_5.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_6.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_7.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_8.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_9.png'))
        self.sprites.append(pygame.image.load('Joao Tinti\Sprites/animation-master/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3,64*3))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar =False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128*3,64*3))

    



todas_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_sprites.add(sapo)
relogio = pygame.time.Clock()

while True:
    relogio.tick(20)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
           sapo.atacar() 
    

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()