import pygame
from ARROW import Arrow
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 200
        self.max_health = 200
        self.vel = 4
        self.all_arrows = pygame.sprite.Group()
        self.attack = 10
        self.image = pygame.image.load("assets/hunter.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        

    def launch_arrow(self):
        the_arrow = Arrow(self)
        self.all_arrows.add(the_arrow)
        


    def move_right(self):
            self.rect.x += self.vel
        
    def move_left(self):
        self.rect.x -= self.vel