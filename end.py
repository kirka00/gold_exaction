import pygame

# test (финальная сцена)
screen = pygame.display.set_mode((800, 600))
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
            textsurface = myfont.render('End Game!', False, ('black'))
            screen.blit(textsurface,(0, 0))
            pygame.display.update()