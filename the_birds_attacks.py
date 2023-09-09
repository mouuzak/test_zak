import pygame
from violent_bird import VIOLENTBIRD

class birdFallEvent:

    def __init__(self, game) :
        self.game = game
        self.percent = 0
        self.percent_speed = 5
        self.all_violentbirds = pygame.sprite.Group()
        self.V_mode = False # the mode when the violent birds attacks

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def launch_Vbirds(self):# Vbirds = Violent birds
        for i in range(1, 5):
            Vbirds = VIOLENTBIRD(self)
            self.all_violentbirds.add(Vbirds)
    
    def attempt_fall(self):
        if self.percent >= 100 and len(self.game.all_birds): # that mean that the percent bar is full
            # bird attack !!!!!!
            self.launch_Vbirds()
            self.reset_percent()
            self.V_mode = True  # launch the attack mode
            


    def update_percent_bar(self, surface):
        # add percent
        self.add_percent()
        # reset the bar if nessesary
        self.attempt_fall()
        # barre en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #coordonnee en x
            surface.get_height() - 20, # coordonnes en y( cela revient a la hauteur de l'ecran dans mon cas)
            surface.get_width(), # longueur de la barre(cela revient a la longueur de l'ecran dans mon cas)
            10 # hauteur de la barre
        ])
        # barre en chargement
        pygame.draw.rect(surface, (187, 11, 11) , [
            0, #coordonnee en x
            surface.get_height() - 20, # coordonnes en y( cela revient a la hauteur de l'ecran dans mon cas)
            (surface.get_width() / 100) * self.percent, # longueur de la barre
            10 # hauteur de la barre
        ])