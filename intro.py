import pygame

# test (начальная сцена)
screen = pygame.display.set_mode((800, 600))
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    intro = False
        if intro:
            screen.fill('white')
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render('Intro', False, ('black'))
            screen.blit(textsurface,(0, 0))
            pygame.display.update()

        

    pygame.quit()
