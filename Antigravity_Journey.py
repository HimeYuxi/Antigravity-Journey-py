import pygame, sys
from pygame.locals import *

from classes import Player
from classes import Platform
from classes import Enemy
from classes import Spikes
from classes import Battery


pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('AntiGravity Journey')

background_music = pygame.mixer.Sound("./Sons/backgroundsound.mp3") #musique de fond
background_music.set_volume(0.3)
background_music.play()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (200, 200, 200)
GREY = (128, 128, 128)
DARK_GREY = (75, 75, 75)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
DARK_RED = (128, 0, 0)
DARK_GREEN = (0, 128, 0)
DARK_BLUE = (0, 0, 128)
ORANGE = (255, 128, 0)

#Ecriture startscreen
def write_text(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def write_shade(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, DARK_GREY)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def start_game(display_surface):
    no_space = True
    while no_space:
        display_surface.fill(GREY)
        write_shade(DISPLAYSURF, 'AntiGravity Journey', 150, 605, 155)
        write_text(DISPLAYSURF, 'AntiGravity Journey', 150, 600, 150)
        write_text(DISPLAYSURF, '[press SPACE to begin]', 100, 600, 375)
        write_text(DISPLAYSURF, 'ALAZRAKI Timothé', 25, 100, 550)
        write_text(DISPLAYSURF, 'PUAUX Alexis', 25, 79, 525)
        write_text(DISPLAYSURF, 'REN Sylvia', 25, 66, 500)
        write_text(DISPLAYSURF, 'QUIRION-CORTEEL Anselme', 25, 139, 575)



        pygame.display.update()
        
        for event in pygame.event.get():# Get system events
            if event.type == pygame.QUIT: # Exit game loop if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    no_space = False

#Ecriture endgame
def write_text_lose(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def write_shade_lose(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, DARK_RED)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

#Ecriture wingame
def write_text_win(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def write_shade_win(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, DARK_GREEN)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

#Son fin de jeu - echec
game_over_sound = pygame.mixer.Sound("./Sons/game_over_sound.mp3")

def end_game(display_surface):
    no_space = True
    while no_space:
        DISPLAYSURF.fill(BLACK)
        write_shade_lose(DISPLAYSURF, 'GAME OVER!', 200, 610, 110)
        write_shade_lose(DISPLAYSURF, 'AntiGravity Journey', 100, 605, 305)
        write_text_lose(DISPLAYSURF, 'GAME OVER!', 200, 600, 100)
        write_text_lose(DISPLAYSURF, 'AntiGravity Journey', 100, 600, 300)
        write_text_lose(DISPLAYSURF, '[press SPACE to restart]', 50, 600, 450)
        write_text_lose(DISPLAYSURF, 'ALAZRAKI Timothé', 25, 100, 550)
        write_text_lose(DISPLAYSURF, 'PUAUX Alexis', 25, 79, 525)
        write_text_lose(DISPLAYSURF, 'REN Sylvia', 25, 66, 500)
        write_text_lose(DISPLAYSURF, 'QUIRION-CORTEEL Anselme', 25, 139, 575)
        write_text_lose(DISPLAYSURF, 'Just in case you forgot:', 25, 100, 475)
        background_music.stop()
        game_over_sound.set_volume(0.3)
        game_over_sound.play()
        pygame.display.update()

        for event in pygame.event.get():# Get system events
            if event.type == pygame.QUIT: # Exit game loop if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    no_space = False


#Son fin de jeu - victoire
victory_sound = pygame.mixer.Sound("./Sons/victory_sound.mp3")

def win_game(display_surface):
    no_space = True
    while no_space:
        DISPLAYSURF.fill(BLACK)
        write_shade_win(DISPLAYSURF, 'YOU WIN!', 200, 610, 110)
        write_shade_win(DISPLAYSURF, 'AntiGravity Journey', 100, 605, 305)
        write_text_win(DISPLAYSURF, 'YOU WIN!', 200, 600, 100)
        write_text_win(DISPLAYSURF, 'AntiGravity Journey', 100, 600, 300)
        write_text_win(DISPLAYSURF, '[press SPACE to exit]', 50, 600, 450)
        write_text_win(DISPLAYSURF, 'ALAZRAKI Timothé', 25, 100, 550)
        write_text_win(DISPLAYSURF, 'PUAUX Alexis', 25, 79, 525)
        write_text_win(DISPLAYSURF, 'REN Sylvia', 25, 66, 500)
        write_text_win(DISPLAYSURF, 'QUIRION-CORTEEL Anselme', 25, 139, 575)
        write_text_win(DISPLAYSURF, 'Just in case you forgot:', 25, 100, 475)
        background_music.stop()
        victory_sound.set_volume(0.3)
        victory_sound.play()

        pygame.display.update()

        for event in pygame.event.get():# Get system events
            if event.type == pygame.QUIT: # Exit game loop if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    no_space = False

        if no_space == False :
            pygame.quit()
            sys.exit()

gravity_sound = pygame.mixer.Sound("./Sons/gravity_sound.mp3") #son de changement de gravite
pressed_keys = pygame.key.get_pressed()

start = True
gravity = True
end = False
victory = False
change = 0

while True: # MAIN GAME LOOP
    DISPLAYSURF.fill(GREY)
    if start:
        start_game(DISPLAYSURF)
        player1 = Player()
        nice_guys = pygame.sprite.Group()
        nice_guys.add(player1)

        wall1 = Platform(400, 25, 0, 300)
        wall2 = Platform(150, 20, 480, 150)
        wall3 = Platform(150, 20, 780, 150)
        wall4 = Platform(250, 25, 960, 360)
        wall5 = Platform(10, 600, 0, 0)
        wall6 = Platform(10, 600, 1190, 0)
        platforms = pygame.sprite.Group()
        platforms.add(wall1, wall2, wall3, wall4, wall5, wall6)

        enemy1 = Enemy(200, 458)
        enemy2 = Enemy(500, 290)
        enemy3 = Enemy(290, 250)
        enemy4 = Enemy(680, 120)
        enemy5 = Enemy(910, 350)
        spikes1 = Spikes(420, 480)
        spikes2 = Spikes(620, 480)
        spikes3 = Spikes(790, 480)
        spikes4 = Spikes(520, 480)
        bad_guys = pygame.sprite.Group()
        bad_guys.add(enemy1, enemy2, enemy3, enemy4, enemy5, spikes1, spikes2, spikes3, spikes4)

        battery = Battery()
        win = pygame.sprite.Group()
        win.add(battery)

        all_sprites= pygame.sprite.Group()
        all_sprites.add(player1, wall1, wall2, wall3, wall4, wall5, wall6, enemy1, enemy2, enemy3, enemy4, enemy5, spikes1, spikes2, spikes3, spikes4, battery)
        print(all_sprites)
        start = False
        
    if end:
        end_game(DISPLAYSURF)
        for sprites in all_sprites:
            sprites.kill()
        print(all_sprites)   
        start = True
        end = False
    if pygame.sprite.spritecollide(player1, bad_guys, False):
        end = True
    if victory:
        win_game(DISPLAYSURF)
    if pygame.sprite.spritecollide(player1, win, False):
        victory = True

    imp = pygame.image.load("./Creations/floor.png")  
    imp2 = pygame.image.load("./Creations/roof.png")
    pygame.transform.scale(imp, (1200, 600))
    pygame.transform.scale(imp2, (1200, 600))
    DISPLAYSURF.blit(imp,(0, 0))
    DISPLAYSURF.blit(imp2,(0, 0))
    nice_guys.draw(DISPLAYSURF)
    bad_guys.draw(DISPLAYSURF)
    win.draw(DISPLAYSURF)
    platforms.draw(DISPLAYSURF)

    keys = pygame.key.get_pressed()

    if (keys[K_RIGHT]):
        player1.move_right(change, platforms)
        change = 0
    if (keys[K_LEFT]):
        player1.move_left(change, platforms)
        change = 1
    if(keys[K_UP]):
        gravity = False
        gravity_sound.set_volume(1.0)
        gravity_sound.play()
    if(keys[K_DOWN]):
        gravity = True
        gravity_sound.set_volume(1.0)
        gravity_sound.play()
    player1.update(gravity, platforms)
    if player1.rect.x > DISPLAYSURF.get_width():
        player1.rect.x = 0 - + player1.rect.width
    if player1.rect.x + player1.rect.width < 0:
        player1.rect.x = DISPLAYSURF.get_width()

    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
