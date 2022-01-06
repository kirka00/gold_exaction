import pygame
from load import screen

def end_game():
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    end = False
        if end:
            screen.fill('white')
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('End Game!', True, ('black'))
            screen.blit(textsurface,(0, 0))
            pygame.display.update()

end_game()