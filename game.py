import pygame
import os
from PLAYER import Player
from pygame.locals import*
from BIRDS import Bird
from sound import SoundManager
from the_birds_attacks import birdFallEvent
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.font.init()

class Game:
    def __init__(self):
        # know if the game is started
        self.is_playing = False
        #  generate the attacking bird event
        self.attack_bird_event = birdFallEvent(self)
        #generate our player
        self.all_birds = pygame.sprite.Group() # create an empty group of birds
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        # to create automatically 6 birds at the start of the game
        '''self.auto_generate() 
        self.auto_generate()
        self.auto_generate()
        self.auto_generate()
        self.auto_generate()'''
        self.auto_generate()
        # define the default value of the score
        self.score = 0

        self.sound_manager = SoundManager()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def start(self):
        self.is_playing = True
        self.auto_generate()
        
    def game_over(self):
        # reboot the game
        self.all_birds = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    

    

    

    def launch_the_game(self, screen, background, player):
        def get_highest_score() :
            with open("highest score.txt", "r") as f :
                return f.read()
        
        try :
            highest_score = int(get_highest_score())
        except :
            highest_score = 0 

        if highest_score < self.score :
            highest_score = self.score
        with open("highest score.txt", "w") as f :
            f.write(str(highest_score))

        

        

         # apply background
        screen.blit(background, (0, 0))

            # apply player
        screen.blit(player.image, player.rect)
    
            # apply th player health bar
        player.update_player_health_bar(screen)
            
        # apply the attacking bird event
        self.attack_bird_event.update_percent_bar(screen)

         # print the score on the screen
        my_font = pygame.font.SysFont("Amasis MT Pro Medium", 40)
        H_score_text = my_font.render(f"high score : {highest_score}", 1, (255, 0, 0))
        score_text = my_font.render(f"score : {self.score}", 1, (255, 170, 51))
        screen.blit(H_score_text, (850, 300))
        screen.blit(score_text, (20, 50))

            # carry all monster movement
        for bird in self.all_birds:
            bird.auto_move()
            bird.update_bird_health_bar(screen)

        for Vbirds in self.attack_bird_event.all_violentbirds:
            Vbirds.auto_attack()
            self.sound_manager.play('birds_attack')

            # apply the birds on the screen
        self.all_birds.draw(screen)
            # apply fireballs on the screen
        player.all_arrows.draw(screen)
            # apply the Vbirds on the screen
        self.attack_bird_event.all_violentbirds.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                pygame.quit()

               # fliped = False

                #throw arrows 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.launch_arrow()
                    self.sound_manager.play('arrow')
                        #carry the fliping
                if event.key == pygame.K_f:
                    player.image = pygame.transform.flip(player.image, True, False) 
                    '''for arrows in player.all_arrows:
                            arrows.image = pygame.transform.rotate(arrows.image, 128)'''
                            #arrows.move_left()


                # carry all arrow movement
                    
        for arrows in player.all_arrows:
            arrows.move_right()
                    #arrows.move_left()
                        # carry the caracther movement
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]  and player.rect.x + player.rect.width < screen.get_width():
             player.move_right()
             
            
        elif keys[K_LEFT]  and player.rect.x > 0:
            player.move_left()
        jumping = False
            # carry the character jumping
        if keys[K_j]: 
            jumping = True

        if jumping :
            player.jump()
        pygame.display.update()

    def auto_generate(self):
        for i in range(1, 3):
            the_bird = Bird(self)
            self.all_birds.add(the_bird) # add a monster in the group