import pygame, sys

######################################## Platform #####################################################

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y):

        super().__init__()

        self.image = pygame.image.load("./Creations/small_wall.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


######################################## Player #####################################################

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
 

        img1 = pygame.image.load("./Creations/robot.png")
        self.image = img1   
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 492

        # speed vector
        self.velocity = 10

# to move the player
    def update(self, g, platforms):
        # gravity
        if g:
            if self.rect.y < 492:
                self.rect.y += self.velocity
                if pygame.sprite.spritecollide(self, platforms, False):
                    self.rect.y -= self.velocity
        else:
            if self.rect.y > 56:
                self.rect.y -= self.velocity
                if pygame.sprite.spritecollide(self, platforms, False):
                    self.rect.y += self.velocity
        
    def reset(self):
        self.rect.x = 100
        self.rect.y = 492

        # move left / right

    def move_right(self, reverse_image, platforms):
        if reverse_image == 1:
            self.image = pygame.transform.flip(self.image, True, False)
        if (not(pygame.sprite.spritecollide(self, platforms, False))) or reverse_image == 1:
            self.rect.x += self.velocity

    def move_left(self, reverse_image, platforms):
        if reverse_image == 0:
            self.image = pygame.transform.flip(self.image, True, False)
        if (not(pygame.sprite.spritecollide(self, platforms, False))) or reverse_image == 0:
            self.rect.x -= self.velocity

######################################## Ennemy #####################################################

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load("./Creations/enemy.png")
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


####################################### Spike ######################################################


        
class Spikes(pygame.sprite.Sprite):
 
    def __init__(self, x, y):

        super().__init__()
 
        self.image = pygame.image.load("./Creations/spikes.png")
        self.image = pygame.transform.scale(self.image,(70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#################################### Battery ##################################

class Battery(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        battery_image = pygame.image.load("./Creations/battery.png")
        self.image = pygame.transform.scale(battery_image,(30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = 720
        self.rect.y = 520
