import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    textFont = pygame.font.Font(#indsæt font, 115)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def crash():
    message_display('You Crashed')
