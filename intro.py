import pygame
from game_play import play
from settings import terminate, default_font, repository, clock, load_image, screen, draw_text, text
import webbrowser


background_image = load_image("background.png")  # установка заднего фона
pygame.mouse.set_visible(False)  # отключение стандартного курсора
cursor = load_image('cur\cursor_standart.png')  # загрузка курсора


class Menu:  # класс меню (делал Фёдор)
    def __init__(self, points):
        self.points = points

    def render(self, powerhost, font, num_points):  # переключение между кнопками и их выделение
        for i in self.points:
            if num_points == i[5]:
                powerhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                powerhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, animation=True, inf=False):  # функция меню
        # загрузка картинок для анимации
        animation_set = [load_image(f"santa{i}.png") for i in range(1, 13)]
        running = True  # флаг для цикла
        points = 0  # переменная для пунктов меню
        n = 0  # переменная для анимациии
        while running:  # цикл меню
            if inf:  # питону тяжело и если резко дёргать мышку он не успевает отрисовывать
                draw_text()  # изображение информации
            pygame.display.update()  # обновление для курсора
            screen.blit(background_image, (0, 0))  # установка фона
            mp = pygame.mouse.get_pos()  # координаты улика мыши
            # анимация Деда Мороза
            if animation:
                screen.blit(animation_set[n // 12], (190, 25))
            n += 1  # обновление переменной для анимации
            if n == 60:
                n = 0
            clock.tick(60)  # фпс для анимации
            for i in self.points:  # выбор мышкой
                if i[0] + 100 > mp[0] > i[0] and i[1] + 50 > mp[1] > i[1]:
                    points = i[5]  # 5 элемент это номер типа int у каждой кнопки он разный
            self.render(screen, default_font, points)  # рендер кнопки
            screen.blit(cursor, mp)  # курсор мыши
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    running = False
                    terminate()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:  # немедленный выход
                        terminate()
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    #  print(points)
                    if points == 0:
                        play()  # запуск игры
                    elif points == 2:
                        support()  # информация
                    elif points == 3:
                        terminate()  # полный выход из программы
                    elif points == 9:
                        intro_func()  # вызов меню
                    elif points == 20:
                        webbrowser.open_new(repository)  # открытие гита
                    elif points == 21:
                        info()  # информация
                pygame.display.flip()
        pygame.quit()


def support():
    points = [(120, 140, f'GitHub', (41, 49, 51), (76, 81, 74), 20),
              (120, 210, u'Information', (41, 49, 51), (76, 81, 74), 21),
              (120, 280, u'Back', (41, 49, 51), (76, 81, 74), 9)]
    game1 = Menu(points)
    game1.menu()


def intro_func():
    points = [(120, 70, u'Game', (41, 49, 51), (76, 81, 74), 0),  # запуск
              (120, 140, u'Support', (41, 49, 51), (76, 81, 74), 2),  # сылка на гит
              (120, 210, u'Quit', (41, 49, 51), (76, 81, 74), 3)]  # выход
    game = Menu(points)
    game.menu()


def info():
    points = [(360, 450, u'Back', (41, 49, 51), (76, 81, 74), 9)]
    game1 = Menu(points)
    game1.menu(False, True)