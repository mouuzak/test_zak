import pygame
pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.vel = 5
        self.attack = 10
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, -9)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx - 30
        self.rect.y = player.rect.centery - 90



    

    def move(self):
        self.rect.x += 2.6
        self.rect.y -= 0.8

        # check if the arrow hit a bird
        #if self.rect.collidepoint()

        