import pygame
from PLAYER import Player
from BIRDS import Bird

class Game:
    def __init__(self):

        #generate our player
        self.all_birds = pygame.sprite.Group() # create an empty group of moster
        self.auto_generate() # to create automatically a monster at the start of the game


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def auto_generate(self):
        the_bird = Bird()
        self.all_birds.add(the_bird) # add a monster in the group