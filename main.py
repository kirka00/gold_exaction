import pygame
from intro import intro_func


def main():  # основная функция игры
    pygame.init()  # Инициализация
    size = scr_width, scr_height = 800, 600  # размеры окна
    screen = pygame.display.set_mode(size)  # установка размеров окна
    pygame.display.set_caption('Stealing gifts')  # заголовок окна
    running = True
    draw = True
    while running:  # основной цикл игры
        for event in pygame.event.get():  # отслеживание действий
            if event.type == pygame.QUIT:  # при закрытии прекращается цикл
                running = False
        if running:
            intro_func()
    pygame.quit()  # закртытие программы


if __name__ == '__main__':  # запуск игры
    main()
