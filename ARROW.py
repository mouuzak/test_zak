import pygame
pygame.init()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, player, game):
        super().__init__()
        self.vel = 5
        self.attack = 10
        self.game = game
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, -9)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx - 30
        self.rect.y = player.rect.centery - 90

    

    
    

    

    def move_right(self):
        self.rect.x += 2.6
        self.rect.y -= 0.8

    
        if self.rect.y < 15:
            self.kill()
        # check if the arrow hit a bird
        '''if self.game.check_collision(self, self.game.all_birds):
            self.remove()'''
        # all the birds who will collide an arrow will be damaged
        for bird in  pygame.sprite.spritecollide(self, self.game.all_birds, False):
            #self.remove()
            bird.get_damage(self.player.attack)
        

    '''def move_left(self):
        self.rect.x += 2.6
        self.rect.y -= 0.8'''
    

       
        #if self.rect.collidepoint()
