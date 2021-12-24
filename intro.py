import sys
import pygame
from game_play import play
from load import load_image

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
bg = load_image("background.png")  # можно убрать если не будет выбора фона в настройках
pygame.mouse.set_visible(False)
cursor = load_image('cur\cursor.png')

class Menu:
    def __init__(self, punkts):
        self.punkts = punkts

    def render(self, powerhost, font, num_punkt):  # переключение между кнопками и их выделение
        for i in self.punkts:
            if num_punkt == i[5]:
                powerhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                powerhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 50)  # шрифт
        punkt = 0
        while done:
            pygame.display.update()

            screen.blit(bg, (0, 0))
            screen.blit(cursor, pygame.mouse.get_pos())
            mp = pygame.mouse.get_pos()
            for i in self.punkts:  # выбор мышкой надо пофиксить но вроде работает как надо
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)  # 1-экран 2-шрифт 3-забыл что
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    done = False
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:  # немедленный выход
                        sys.exit()
                    if i.key == pygame.K_UP:  # переключение между кнопками стрелочками
                        if punkt > 0:
                            punkt -= 1
                        elif punkt == 0:
                            punkt = 3
                    if i.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                        elif punkt == 3:
                            punkt = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if punkt == 0:
                        play()
                    elif punkt == 1:
                        settings()
                    elif punkt == 2:
                        sys.exit()
                    elif punkt == 6:
                        intro_func()
                pygame.display.flip()
        pygame.quit()


def settings():
    punkts2 = [(120, 140, u'Что-то', (41, 49, 51), (76, 81, 74), 5),
               (120, 210, u'Back', (41, 49, 51), (76, 81, 74), 6)]
    game1 = Menu(punkts2)
    game1.menu()


def intro_func():
    punkts = [(120, 70, u'Game', (41, 49, 51), (76, 81, 74), 0),  # запуск
              (120, 140, u'Settings', (41, 49, 51), (76, 81, 74), 1),  # настройки
              (120, 210, u'Quit', (41, 49, 51), (76, 81, 74), 2),  # выход
              (120, 280, u'Support', (41, 49, 51), (76, 81, 74), 3)]  # поддержка
    game = Menu(punkts)
    game.menu()