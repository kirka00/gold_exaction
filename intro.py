import sys
import pygame
from game_play import play

screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
bg = pygame.image.load("data/bg_for_menu.png")  # можно убрать если не будет выбора фона в настройках
pygame.mouse.set_visible(False)
cursor = pygame.image.load('data/img_1.png')


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
        pygame.font.init()
        font_menu = pygame.font.Font('Oswald/static/Oswald-Light.ttf', 50)  # шрифт
        punkt = 0
        screen.blit(bg, (0, 0))
        while done:
            try:  # костыль надо убрать
                if pygame.mouse.get_focused():
                    screen.blit(bg, (0, 0))
                    screen.blit(cursor, pygame.mouse.get_pos())
                mp = pygame.mouse.get_pos()
                for i in self.punkts:  # выбор мышкой надо пофиксить но вроде работает как надо
                    if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                        punkt = i[5]
                self.render(screen, font_menu, punkt)  # 1-экран 2-шрифт 3-забыл что
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
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
                            done = False
                        elif punkt == 6:
                            intro()
                    pygame.display.flip()
            except Exception:
                pass
        pygame.quit()


def intro():  # в punkts 1 корды потом что будет написано и 2 кортежа в 1 цвет когда не выбраны а во 2 когда выбраны ласт номер
    punkts = [(120, 70, u'Game', (41, 49, 51), (76, 81, 74), 0),  # запуск
              (120, 140, u'Settings', (41, 49, 51), (76, 81, 74), 1),  # настройки
              (120, 210, u'Quit', (41, 49, 51), (76, 81, 74), 2),  # выход
              (120, 280, u'Support', (41, 49, 51), (76, 81, 74), 3)]  # поддержка
    game = Menu(punkts)
    game.menu()


def settings():
    punkts2 = [(120, 140, u'Что-то', (41, 49, 51), (76, 81, 74), 5),
               (120, 210, u'Back', (41, 49, 51), (76, 81, 74), 6)]
    game1 = Menu(punkts2)
    game1.menu()


intro()