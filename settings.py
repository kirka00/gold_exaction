import pygame
import sys
import os


def draw_text(text1, text2):  # вывод сообщения на экран
    conclusion1 = small_font.render(
        f'{text1}', True, 'black')
    conclusion2 = small_font.render(
        f'{text2}', True, 'black')
    screen.blit(conclusion1, (350, 300))
    screen.blit(conclusion2, (0, 0))


def load_image(name, colorkey=None):  # загрузка текстур
    fullname = os.path.join('data/images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):  # загрузка уровня
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


# основные настройки
pygame.init()  # инициализация для шрифта
screen = pygame.display.set_mode([800, 600])  # установка размеров окна
size = scr_width, scr_height = 800, 600  # размеры окна
clock = pygame.time.Clock()
default_font = pygame.font.Font(
    'data/Oswald/static/Oswald-Light.ttf', 40)  # стандартный шрифт
large_font = pygame.font.Font(
    'data/Oswald/static/Oswald-Light.ttf', 50)  # большой шрифт
small_font = pygame.font.Font(
    'data/Oswald/static/Oswald-Light.ttf', 25)  # большой шрифт
pygame.display.set_icon(load_image("tree.png"))
repository = 'https://github.com/kirka00/stealing_gifts/'


def terminate():  # закрытие программы
    pygame.quit()
    sys.exit()
