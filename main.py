import pygame
from intro_func import intro_func
#from end import end_game
'''from levels import Level_1, Level_2, Level_3
from player import Player'''


def main():  # основная функция игры
    pygame.init()  #  Инициализация
    width, height = 800, 600  # размеры окна
    screen = pygame.display.set_mode((width, height))  # установка размеров окна
    pygame.display.set_caption('Gold exaction')  # заголовок окна
    running = True  # основной цикл игры
    '''player = Player()  # создание героя
    levels = []  # создание уровней
    levels.append(Level_1(player))  # добавление героя'''

    while running:
        for event in pygame.event.get():  # отслеживание действий
            if event.type == pygame.QUIT:  # при закрытии прекращается цикл
                running = False
        intro_func()
    #  pygame.quit()  # закрытие программы


if __name__ == '__main__':  # запуск игры
    main()