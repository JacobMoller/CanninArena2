import pygame
pygame.init()
displayWidth = infoObject.current_w
displayHeight = int(infoObject.current_h * 0.9)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

pygame.display.update()
