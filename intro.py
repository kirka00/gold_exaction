import sys
import pygame
from game_play import play
from load import load_image, screen
from settings import terminate, default_font, repository, clock
import webbrowser


background_image = load_image("background.png")
pygame.mouse.set_visible(False)
cursor = load_image('cur\cursor.png')


class Menu:  # класс меню (делал Фёдор)
    def __init__(self, pointss):
        self.pointss = pointss

    def render(self, powerhost, font, num_points):  # переключение между кнопками и их выделение
        for i in self.pointss:
            if num_points == i[5]:
                powerhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                powerhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):  # функция меню
        # загрузка картинок для анимации
        animation_set = [load_image(f"santa{i}.png") for i in range(1, 13)]
        running = True  # флаг для цикла
        points = 0  # переменная для пунктов меню
        n = 0  # переменная для анимациии
        while running:  # цикл меню
            pygame.display.update()  # обновление для курсора
            screen.blit(background_image, (0, 0))  # установка фона
            mp = pygame.mouse.get_pos()  # координаты улика мыши
            screen.blit(cursor, mp)  # курсор мыши
            # анимация Деда Мороза
            screen.blit(animation_set[n // 12], (190, 25))
            n += 1  # обновление переменной для анимации
            if n == 60:
                n = 0
            clock.tick(60)  # фпс для анимации
            for i in self.pointss:  # выбор мышкой надо пофиксить но вроде работает как надо
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    points = i[5]
            # 1-экран 2-шрифт 3-забыл что
            self.render(screen, default_font, points)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    running = False
                    terminate()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:  # немедленный выход
                        terminate()
                    if i.key == pygame.K_UP:  # переключение между кнопками стрелочками
                        if points > 0:
                            points -= 1
                        elif points == 0:
                            points = 3
                    if i.key == pygame.K_DOWN:
                        if points < len(self.pointss) - 1:
                            points += 1
                        elif points == 3:
                            points = 0
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if points == 0:
                        play()
                    elif points == 1:
                        support()
                    elif points == 2:
                        terminate()
                    elif points == 5:
                        webbrowser.open_new(repository)
                    elif points == 6:
                        intro_func()
                pygame.display.flip()
        pygame.quit()


def support():
    global repository
    pointss2 = [(120, 140, f'GitHub', (41, 49, 51), (76, 81, 74), 5),
                (120, 210, u'Back', (41, 49, 51), (76, 81, 74), 6)]
    game1 = Menu(pointss2)
    game1.menu()


def intro_func():
    pointss = [(120, 70, u'Game', (41, 49, 51), (76, 81, 74), 0),  # запуск
               (120, 140, u'Support', (41, 49, 51), (76, 81, 74), 1),  # настройки
               (120, 210, u'Quit', (41, 49, 51), (76, 81, 74), 2)]  # выход
    game = Menu(pointss)
    game.menu()
