import pygame
import sys
from load import load_image
# настройки экрана
pygame.init()  # инициализация для шрифта
size = scr_width, scr_height = 800, 600  # размеры окна
clock = pygame.time.Clock()
default_font =  pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 40)  # стандартный шрифт
large_font = pygame.font.Font('data/Oswald/static/Oswald-Light.ttf', 50)  # большой шрифт
pygame.display.set_icon(load_image("tree.png"))


def terminate():  # закрытие программы
    pygame.quit()
    sys.exit()