import pygame,sys
from pygame.locals import *

from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP

background_music = pygame.mixer.Sound("./Sons/backgroundsound.mp3") #musique de fond
background_music.set_volume(0.50)
background_music.play()

gravity_sound = pygame.mixer.Sound("./Sons/gravity_sound.mp3") #son de changement de gravite

game_over_sound = pygame.mixer.Sound("./Sons/game_over_sound.mp3") #son game over

victory_sound = pygame.mixer.Sound("./Sons/victory_sound.mp3") #son victoire

pressed_keys = pygame.key.get_pressed()

if pressed_keys[KEY_UP] or pressed_keys[KEY_DOWN]:
    gravity_sound.set_volume(0.50)
    gravity_sound.play()
    
if victory == True :
    victory_sound.set_volume(0.50)
    victory_sound.play()
    
if death == True :
    game_over_sound.set_volume(0.50)
    game_over_sound .play()