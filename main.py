import pygame
from pygame.locals import*
from BIRDS import Bird
from PLAYER import Player
from game import Game

pygame.init()

Title = pygame.display.set_caption(" hunter game")
screen = pygame.display.set_mode((1080,600))

bg = pygame.image.load("assets/forest1.png")
background = pygame.transform.scale(bg, (1080, 700))


game = Game()
player = Player(game)

running = True
while running:
    
    # apply background
    screen.blit(background, (0, 0))

    # apply player
    screen.blit(player.image, player.rect)
    # carry all fireball movement
    for arrows in player.all_arrows:
        arrows.move()
       

    # apply fireballs on the screen
    player.all_arrows.draw(screen)

    # carry all monster movement
    for monster in game.all_birds:
        monster.auto_move()


    # apply the monster on the screen
    game.all_birds.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()

        #throw fireball 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.launch_arrow()

        # register user's imput
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and player.rect.x + player.rect.width < screen.get_width():
            player.move_right()
    
    elif keys[K_LEFT] and player.rect.x > 0:
            player.move_left()




    # carry the character flipping 
    to_right = True
    if player.rect.x > screen.get_width()/ 2 and to_right == True :
         player.image = pygame.transform.flip(player.image, True, False)
         to_right= False
    if player.rect.x >  20 and to_right == False :
        player.image = pygame.transform.flip(player.image, True, False)
        to_right = True
            
    

                
        





        # carry player movement
        



    pygame.display.update()