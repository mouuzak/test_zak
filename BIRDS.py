import pygame


# create the monster class

class Bird(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.vel = 2
        self.image = pygame.image.load("assets/bird.png")
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 10



    def auto_move(self):
        self.rect.x += self.vel
       
