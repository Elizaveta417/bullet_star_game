import pygame
import random



class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(f'image/butterfly.png')
        self.image = pygame.transform.rotozoom(self.image, 1,0.09)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(1,800)
        self.rect.centery = 0
        self.speedx = 0
        self.speedy = 3


    def update(self):
        self.move()
        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y += self.speedy







