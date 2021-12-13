import sys
import pygame

screen = pygame.display.set_mode((400, 400))


class Menu:
    def __init__(self, punkts=[(120, 140, u'Punkt', (250, 250, 30), (250, 30, 250))]):
        self.punkts = punkts

    def render(self, powerhost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                powerhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                powerhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        pygame.font.init()
        font_menu = pygame.font.Font('Oswald-Light.ttf', 50)  # шрифт
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        sys.exit()
                    if i.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if i.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

        #  window.blit(screen, (0, 0))
            pygame.display.flip()


punkts = [(120, 70, u'Game', (250, 250, 30), (250, 30, 250), 0),
          (120, 140, u'Settings', (250, 250, 30), (250, 30, 250), 1),
          (120, 210, u'Quit', (250, 250, 30), (250, 30, 250), 2),
          (120, 280, u'Support', (250, 250, 30), (250, 30, 250), 3)]
game = Menu(punkts)
game.menu()