import pygame
import sys
from load import load_image, screen
# настройки экрана
pygame.init()  # инициализация для шрифта
size = scr_width, scr_height = 800, 600  # размеры окна
clock = pygame.time.Clock()
default_font =  pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 40)  # стандартный шрифт
large_font = pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 50)  # большой шрифт
small_font = pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 25)  # большой шрифт
pygame.display.set_icon(load_image("tree.png"))
repository = 'https://github.com/kirka00/stealing_gifts/'


def terminate():  # закрытие программы
    pygame.quit()
    sys.exit()


def draw_text(text1, text2):  # вывод сообщения на экран
        conclusion1 = small_font.render(
            f'{text1}', True, 'black')
        conclusion2 = small_font.render(
            f'{text2}', True, 'black')
        screen.blit(conclusion1, (350, 300))
        screen.blit(conclusion2, (0, 0))