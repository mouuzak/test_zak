import pygame
import random
import animation


# create the monster class

class Bird(pygame.sprite.Sprite):
    def __init__(self, game): 
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.vel = 2 + random.randint(0, 5)
        self.image = pygame.image.load("assets/bird.png")
        self.rect = self.image.get_rect()
        self.rect.x = 2 + random.randint(0, 5)
        self.rect.y = 20 - random.randint(1, 5)

    def get_damage(self, amount): # amount represent the amount of damage that the bird will get if he get hit by an arrow
        self.health -= amount

        # create him as a new bird
        if self.health <= 0 :
            self.rect.x = 2 + random.randint(0, 5)
            self.rect.y = 20 - random.randint(1, 5)
            self.vel = 2 + random.randint(0, 5)
            self.health = self.max_health
            # update the score
            self.game.score += 10




    def update_animation(self):
        self.animate()


    def update_bird_health_bar(self, surface):
        #note: the order you use to draw the rect is important
        #create the rect behind the health bar
        pygame.draw.rect(surface, ( 0, 0 ,0 ),[self.rect.x, self.rect.y,self.max_health, 5])
        # create the health bar
        # to draw a rect : pygame.draw.rect(the surface, the rect color, [x coordinate, y coordinate, the rect width, the rect height])
        pygame.draw.rect(surface, ( 110, 210 ,46 ),[self.rect.x, self.rect.y,self.health, 5])
        
        



    def auto_move(self):
        self.rect.x += self.vel
        if self.rect.x > 1080 : # 1080 is the screen width
            self.rect.x = 0 + random.randint(1, 5)
            self.rect.y = 20 - random.randint(1, 5)
            self.vel = 2 + random.randint(0, 5)
       
