import pygame
from pygame.locals import*
from BIRDS import Bird
from PLAYER import Player
from game import Game
pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

Title = pygame.display.set_caption(" hunter game")
screen = pygame.display.set_mode((1080,600))
my_icon = pygame.image.load("assets/Game_icon.png")
pygame.display.set_icon(my_icon)

clock = pygame.time.Clock()

bg = pygame.image.load("assets/forest1.png")
background = pygame.transform.scale(bg, (1080, 700))
# load the banner
banner = pygame.image.load("assets/the banner.png")
banner = pygame.transform.scale(banner, (1080, 600))
# load the play button
launch_button = pygame.image.load("assets/button.png")
launch_button = pygame.transform.scale(launch_button, (400, 150))
launch_button_rect = launch_button.get_rect()

game = Game()     


running = True
while running:
    
    clock.tick(60)
    # verify if the game has begin
    if game.is_playing:
        # launch the game      
        game.launch_the_game(screen, background, game.player)
    else:
        screen.blit(banner, (0, 0))
        screen.blit(launch_button, (300, 320))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
                pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                game.start()
            '''if event.type == pygame.MOUSEBUTTONDOWN: 
                if launch_button_rect.collidepoint(event.pos):
                    game.is_playing = True'''
        
        # carry player movement
        

    pygame.display.update()                       