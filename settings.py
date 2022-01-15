import pygame
import sys
import os


def draw_text(text, coords):  # вывод сообщения на экран
    conclusion1 = default_font.render(
        f'{text}', True, (0, 0, 0))
    screen.blit(conclusion1, coords)


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
font1 = pygame.font.Font(
    'data/fonts/Oswald-Bold.ttf', 40)
font2 = pygame.font.Font(
    'data/fonts/Oswald-ExtraLight.ttf', 40)
font3 = pygame.font.Font(
    'data/fonts/Oswald-Medium.ttf', 40)
font4 = pygame.font.Font(
    'data/fonts/Oswald-Regular.ttf', 40)
font5 = pygame.font.Font(
    'data/fonts/Oswald-SemiBold.ttf', 40)
font6 = pygame.font.Font(
    'data/fonts/Oswald-Light.ttf', 40)

# основные настройки
screen = pygame.display.set_mode([800, 600])  # установка размеров окна
size = scr_width, scr_height = 800, 600  # размеры окна
clock = pygame.time.Clock()
pygame.display.set_icon(load_image("tree.png"))
repository = 'https://github.com/kirka00/stealing_gifts/'
text1 = [['Для взаимодействия с объектами нажимайте кнопку E', (0, 0)],
        ['Управлять персонажем можно с помощью wasd', (0, 100)],
        ['shift - рывок в направлении движения игрока', (0, 200)],
        ['пробел - прыжок', (0, 300)]]  # текст для информации в настройках
text2 = [['', (0, 0)],
         ['', (0, 0)],
         ['', (0, 0)],
         ['', (0, 0)]]  # текст для визуализации изменение настройек


def terminate():  # закрытие программы
    pygame.quit()
    sys.exit()