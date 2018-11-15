import pygame
import os, sys
import random
import time

img_path = os.path.join('C:\Python27', 'player.png')
img_path2 = os.path.join('C:\Python27', 'rock.png')

class Bird(object):  
    def __init__(self):           
        self.image_s = pygame.image.load(img_path)
        self.image_b = self.image_s.get_rect()
        self.x = 0
        self.y = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 2 
        if key[pygame.K_DOWN]:
            self.y += dist 
        elif key[pygame.K_UP]: 
            self.y -= dist
        if key[pygame.K_RIGHT]: 
            self.x += dist 
        elif key[pygame.K_LEFT]:
            self.x -= dist 

   def draw(self, surface):
       surface.blit(self.image, (self.x, self.y))

    def background(self, surface):
        bg = os.path.join('C:\Python27', 'bg.png')
        self.image2 = pygame.image.load(bg)
        surface.blit(self.image2, (0,0))

class Rock(object): 
    def __init__(self, x=640, y=0,):
        self.image_s = pygame.image.load(img_path2)
        self.image_b = self.image_s.get_rect()
        self.x = x
        self.y = y
        dist = 10
        self.dist = dist

    def rock(self):
        dist = 10
        self.x -=dist

    def rock_draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            sys.exit()

pygame.init()
screen = pygame.display.set_mode((640, 200))

bird = Bird() 
rock = Rock()
clock = pygame.time.Clock()


running = True
while running:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if rock.x < 0:
            y = random.randint(10, 190)
            rock = Rock(640, y)
        rock.checkCollision(bird.image_b, rock.image_b)

    bird.handle_keys()     
    rock.rock()

    screen.fill((255,255,255))
    bird.background(screen)
    bird.draw(screen)
    rock.rock_draw(screen)
    pygame.display.update() 

    clock.tick(40)
