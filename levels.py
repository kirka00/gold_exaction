from race import racing
from load import load_image, load_level, screen
import pygame
from settings import small_font
from json import dump
flag_on_lvl2 = True
coins = 0


class BlockBricks(pygame.sprite.Sprite):  # класс для платформ
    def __init__(self, width, height):
        super().__init__()
        self.image = load_image('brick.png')  # изображение платформы
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width, self.rect.height = width, height


class Cookie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('cookie.png')  # изображение платформы
        self.rect = self.image.get_rect()  # установка размеров


class Presents(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('present.png')  # изображение платформы
        self.rect = self.image.get_rect()  # установка размеров


class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image('pipe.png')  # изображение платформы
        self.rect = self.image.get_rect()  # установка размеров


class Level(object):  # класс для уровня
    def __init__(self, player, name):
        self.player = player  # сам игрок
        self.platforms = pygame.sprite.Group()  # группа спрайтов
        self.cookies = pygame.sprite.Group()
        self.presents = pygame.sprite.Group()
        self.coords_objects = []  # 0 - труба 1 - печенька 2 - подарок
        lvl_1 = load_level(name)  # преобразование уровня в текст
        for i in range(len(lvl_1)):
            for j in range(len(lvl_1[i])):
                if lvl_1[i][j] != '2' and lvl_1[i][j] != '3' and lvl_1[i][j] != '0':
                    if lvl_1[i][j] == '1':
                        block = BlockBricks(32, 32)
                    elif lvl_1[i][j] == '6':
                        block = Pipe()
                        self.coords_objects.append((j, i - 2))  # добавление координат трубы
                    elif lvl_1[i][j] == '9':
                        block = BlockBricks(0, 0)
                    block.rect.x, block.rect.y = j * 32, i * 32 + 24  # координата x и y
                    self.platforms.add(block)  # добавление в группу
                elif lvl_1[i][j] == '2':
                    cok = Cookie()
                    cok.rect.x, cok.rect.y = j * 32, i * 32 + 24  # координата x и y
                    self.cookies.add(cok)  # добавление в группу
                    self.coords_objects.append((j, i - 1))  # добавление координат печеньки
                elif lvl_1[i][j] == '3':
                    pres = Presents()
                    pres.rect.x, pres.rect.y = j * 32, i * 32 + 24   # координата x и y
                    self.presents.add(pres)  # добавление в группу
                    self.coords_objects.append((j, i - 1))  # добавление координат подарка

    def draw(self, screen):  # рисовка объектов
        screen.blit(load_image('back_game3.png'), (0, 0))  # задний фон
        self.platforms.draw(screen)  # отрисовка блоков
        self.cookies.draw(screen)  # отрисовка печенек
        self.presents.draw(screen)  # отрисовка подарков

    def update(self):  # обновление экрана
        self.platforms.update()

    def clear(self):  # очистка уровня для инициализации нового
        self.platforms.remove()
        self.cookies.remove()
        self.presents.remove()

    def cookies_delete(self):  # remove не работает выходит только через kill
        for i in self.cookies:
            i.kill()

    def presents_delete(self):  # remove не работает выходит только через kill
        for i in self.presents:
            i.kill()

    def coords(self):
        return self.coords_objects


def check(coords, lvl):  # проверка для перехода на след лвл
    global coins, flag_on_lvl2
    cor, cor1 = (coords[0] // 32, (coords[1] - 24) // 32), lvl.coords()  # преобразовка для удобства
    if cor == cor1[1]:  # проверка находится ли игрок на печеньке
        coins += 30
        lvl.cookies_delete()
    elif cor == cor1[2]:  # проверка находится ли игрок на подарке
        coins += 30
        lvl.presents_delete()
    elif cor == cor1[0]:  # проверка находится ли игрок на трубе
        coins += 30
        if not flag_on_lvl2:  # костыль убрать надо
            racing()
        else:
            flag_on_lvl2 = False
            return True
    render_coins(coins)  # отрисовкка монет
    save_in_coins_txt(coins)  # сохранение монет в текстовый файл для статистики


def render_coins(coins):  # отображение монет
    conclusion = small_font.render(
        f'Количество очков: {coins}', True, 'black')
    screen.blit(conclusion, (100, 100))


def save_in_coins_txt(coins):  # сохранение очков в coins.txt
    with open('coins.txt', encoding='utf8', mode='w') as file:
        dump(coins, file)