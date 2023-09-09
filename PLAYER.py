import pygame
from ARROW import Arrow
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 200
        self.max_health = 200
        self.vel = 8
        self.all_arrows = pygame.sprite.Group()
        self.attack = 10
        self.image = pygame.image.load("assets/hunter.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 370
        self.jump_height = 20
        self.gravity = 1
        self.y_vel = self.jump_height


    def suffering(self, amount):
        self.health -= amount
        if self.health <= 0 :
            self.game.game_over()
        
    def update_player_health_bar(self, surface):
        #note: the order you use to draw the rect is important
        #create the rect behind the health bar
        pygame.draw.rect(surface, ( 0, 0 ,0 ),[self.rect.x, self.rect.y,self.max_health, 5])
        # create the health bar
        # to draw a rect : pygame.draw.rect(the surface, the rect color, [x coordinate, y coordinate, the rect width, the rect height])
        pygame.draw.rect(surface, ( 110, 210 ,46 ),[self.rect.x, self.rect.y,self.health, 5])

    def launch_arrow(self):
        the_arrow = Arrow(self, self.game)
        self.all_arrows.add(the_arrow)
        
    def move_right(self):
            self.rect.x += self.vel
        
    def move_left(self):
        self.rect.x -= self.vel

    def jump(self):
        
        self.rect.y -= self.y_vel
        self.y_vel -= self.gravity
        if self.y_vel < -self.jump_height :
            jumping = False
            self.y_vel = self.jump_height
                
                
           
            

        
