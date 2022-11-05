#import libaries
import pygame
import random

#initalize ppygame
pygame.init()

#game window dimensions
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 160

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#game variables
GRAVITY = 1
MAX_WATER = 100


#create game window
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Nosalgia')

#define colors
WHITE = (255, 255, 255)


#loadimages
mario_image = pygame.image.load('New Attempt/Assets/mario.png').convert_alpha()
bg_image = pygame.image.load('New Attempt/Assets/background.png').convert_alpha()
water_image = pygame.image.load('New Attempt/Assets/Foreground.png').convert_alpha()


#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(mario_image, (20, 20))
        self.width = 15
        self.height = 15
        self.rect = pygame.Rect(0,0, self.width + 4, self.height + 4)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        #reset variable
        dx = 0
        dy = 0


        #process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx  = -1
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = 1
            self.flip = False
        if key[pygame.K_SPACE]: # Need to fix this
            self.rect.x += 1

        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player doesn't go off screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_HEIGHT:
            dx = SCREEN_HEIGHT - self.rect.right
        

        #check collision with ground
        if self.rect.bottom + dy > SCREEN_WIDTH:
            dy = 0
            self.vel_y = -5
        
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, WHITE, self.rect, 1)

#Water class
class Water(pygame.sprite.Sprite):
    def __init__(self, x, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(water_image, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x



#Player instance
mario_image = Player(SCREEN_WIDTH // 9, SCREEN_HEIGHT - 890)

#create sprite groups
water_group = pygame.sprite.Group()

#create temporary water
for w in range(MAX_WATER):
    w_width = random.randint(100, 100)
    w_x = random.randint(0, SCREEN_WIDTH - w_width)
    water = Water(w_x, w_width)
    water_group.add(water)




#game loop
run = True
while run:

    clock.tick(FPS)
    mario_image.move()


    #draw background
    screen.blit(bg_image, (0,0))

    #draw sprites
    water_group.draw(screen)
    mario_image.draw()


    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()