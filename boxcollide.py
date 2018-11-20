import pygame, sys, random
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BOX_WIDTH = 20
BOX_HEIGHT = 20
BOX_COUNT = 3
 
class Box(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BOX_WIDTH, BOX_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    def update(self):
        self.rect.y += 1
        if (self.rect.y > SCREEN_HEIGHT):
            self.rect.y = -1 * BOX_HEIGHT
 
pygame.init()
pygame.display.set_caption('Collision Example using simple sprite group')
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
 
pygame.mouse.set_visible(False)
 
just_black_boxes = pygame.sprite.Group()
all_the_boxes = pygame.sprite.Group()
 
# creating and adding black boxes
for i in range(BOX_COUNT):
    tmpx = random.randrange(0, SCREEN_WIDTH)
    tmpy = random.randrange(0, SCREEN_HEIGHT)
    tmpbox = Box(black, [tmpx, 200])
    just_black_boxes.add(tmpbox)
    all_the_boxes.add(tmpbox)
 
# adding a player
player = Box(red, [0, 0])
all_the_boxes.add(player)
x = 400;
x_change = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change += -15
            if event.key == pygame.K_d:
                x_change += 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change += 15
            if event.key == pygame.K_d:
                x_change += -15

    x += x_change
    player.rect.topleft = (x,380)
    just_black_boxes.update()
 
    # checking if player collides with any black boxes
    # if collision happends remove the black box from the group
    test = pygame.sprite.spritecollide(player, just_black_boxes, True)
    if test == True:
        print("u dead boi")
 
    screen.fill(white)
 
    all_the_boxes.draw(screen)
 
    pygame.display.update()
    clock.tick(20)
