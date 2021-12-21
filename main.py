import pygame
#from intro import game_intro  # начальный экран
from game_play import play  # первые уровни

def main():  # основная функция игры
    pygame.init()  #  Инициализация
    size = scr_width, scr_height = 800, 600  # размеры окна
    screen = pygame.display.set_mode(size)  # установка размеров окна
    pygame.display.set_caption('Gold exaction')  # заголовок окна
    running = True  
    while running:  # основной цикл игры
        for event in pygame.event.get():  # отслеживание действий
            if event.type == pygame.QUIT:  # при закрытии прекращается цикл
                running = False
        if running:
            #game_intro()  # интро игры
            play()  # бета уровень
    pygame.quit()  # закртытие программы


if __name__ == '__main__':  # запуск игры
    main()