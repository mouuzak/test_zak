import pygame
import random

from PLAYER import Player
pygame.init()


class VIOLENTBIRD(pygame.sprite.Sprite):
    def __init__(self, the_birds_attacks):
        super().__init__()
        self.image = pygame.image.load("assets/bird attack.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.x = 10 + random.randint(0, 1000)
        self.rect.y = -10
        self.velocity = 4 + random.randint(0, 6)
        self.the_birds_attacks = the_birds_attacks
        #self.player = player
        self.attack = 10

    def Vbird_remove(self):
        self.the_birds_attacks.all_violentbirds.remove(self)

    def auto_attack(self):
        self.rect.y += self.velocity
        if self.rect.y > 500 : # 500 represent the y coordinate of the ground
            self.Vbird_remove()

        if self.the_birds_attacks.game.check_collision(
            self, self.the_birds_attacks.game.all_player
        ):
            self.Vbird_remove()
            self.the_birds_attacks.game.player.suffering(self.attack)



        ''' for player in  pygame.sprite.spritecollide(self, self.player, False):
            #self.remove()
            player.suffering(self.attack)'''
