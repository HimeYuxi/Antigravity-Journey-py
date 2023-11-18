import pygame, sys

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Antigravity Journey')

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

def write_text_lose(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

def write_shade_lose(surface, text, size, x, y):
    FontStyle = pygame.font.match_font('freesansbold.ttf')
    font = pygame.font.Font(FontStyle, size)
    text_surface = font.render(text, True, DARK_RED)
    text_rect = text_surface.get_rect() 
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)


def end_game(display_surface):
    no_space = True
    while no_space:
        DISPLAYSURF.fill(BLACK)
        write_shade_lose(DISPLAYSURF, 'YOU LOSE!', 200, 610, 110)
        write_shade_lose(DISPLAYSURF, 'Antigravity Journey', 100, 605, 305)
        write_text_lose(DISPLAYSURF, 'YOU LOSE!', 200, 600, 100)
        write_text_lose(DISPLAYSURF, 'Antigravity Journey', 100, 600, 300)
        write_text_lose(DISPLAYSURF, '[press SPACE to restart]', 50, 600, 450)

        pygame.display.update()

        for event in pygame.event.get():# Get system events
            if event.type == pygame.QUIT: # Exit game loop if window closed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    no_space = False
