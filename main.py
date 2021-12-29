import pygame
from intro import intro_func
from settings import size
from load import load_image

screen = pygame.display.set_mode(size)  # установка размеров окна
def main():  # основная функция игры
    pygame.init()  # Инициализация
    pygame.display.set_caption('Stealing gifts')  # заголовок окна
    game_icon = load_image('tree.png')
    pygame.display.set_icon(game_icon)
    running = True
    while running:  # основной цикл игрыgame_icon
        for event in pygame.event.get():  # отслеживание действий
            if event.type == pygame.QUIT:  # при закрытии прекращается цикл
                running = False
        if running:
            intro_func()
    pygame.quit()  # закртытие программы


if __name__ == '__main__':  # запуск игры
    main()
