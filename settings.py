import pygame
import sys
import os


def draw_text():  # вывод сообщения на экран
    for i in text:
        conclusion1 = default_font.render(
            i[0], True, (0, 0, 0))
        screen.blit(conclusion1, i[1])


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


pygame.init()  # инициализация для шрифтов
default_font = pygame.font.Font(
    'data/fonts/Oswald-Light.ttf', 40)  # стандартный шрифт
# основные настройки
screen = pygame.display.set_mode([800, 600])  # установка размеров окна
size = scr_width, scr_height = 800, 600  # размеры окна
clock = pygame.time.Clock()
pygame.display.set_icon(load_image("tree.png"))
repository = 'https://github.com/kirka00/stealing_gifts/'
text = [['Для взаимодействия с объектами нажимайте кнопку E', (10, 0)],
        ['Управлять персонажем можно с помощью стрелочек', (10, 100)],
        ['пробел - прыжок', (10, 200)]]  # текст для информации в настройках


def terminate():  # закрытие программы
    pygame.quit()
    sys.exit()