import pygame

pygame.init()

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("canninRunAnimation")

white = (255,255,255)

clock = pygame.time.Clock()

# Mario sprites
c1 = pygame.image.load("Art/cannin/Skin/cannin_default.png")
c2 = pygame.image.load("Art/cannin/Skin/cannin_red.png")

canninCurrentImage = 1

gameLoop=True
while gameLoop:

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False

    window.fill(white)

    if canninCurrentImage==1:
        window.blit(c1, (10,10))

    if canninCurrentImage==2:
        window.blit(c2, (10,10))


    if canninCurrentImage==2:
        canninCurrentImage=1

    else:
        canninCurrentImage+=1;

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
