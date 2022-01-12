from race import racing
import pygame
from settings import small_font, load_image, load_level, screen
from json import dump
cookies = pygame.sprite.Group()
presents = pygame.sprite.Group()
delete = False
delete1 = False
coins = 0
cookie = ''
present = ''
pipe = ''


class BlockBricks(pygame.sprite.Sprite):  # класс для платформ
    image = load_image('brick.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width = width
        self.rect.height = height


class Cookie(pygame.sprite.Sprite):
    image = load_image('cookie.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width = 32
        self.rect.height = 32


class Presents(pygame.sprite.Sprite):
    image = load_image('present.png')  # изображение платформы

    def __init__(self, width, height, group):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.add(group)
        self.rect.width = 30
        self.rect.height = 30


class Pipe(pygame.sprite.Sprite):
    image = load_image('pipe.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров


class Level(object):  # класс для уровня
    def __init__(self, player):
        self.player = player  # сам игрок
        self.platforms = pygame.sprite.Group()  # группа спрайтов

    def draw(self, screen):  # рисовка объектов
        global cookies, presents
        screen.blit(load_image('back_game3.png'), (0, 0))  # задний фон
        self.platforms.draw(screen)  # платформы
        cookies.draw(screen)
        presents.draw(screen)

    def update(self):  # обновление экрана
        self.platforms.update()


class DemoLevel1(Level):
    def __init__(self, player):
        global cookies, presents, cookie, present, pipe
        Level.__init__(self, player)  # наследуем игрока
        lvl_1 = load_level('level1.txt')  # преобразование уровня в текст
        for i in range(len(lvl_1)):
            for j in range(len(lvl_1[i])):
                if lvl_1[i][j] != '2' and lvl_1[i][j] != '3' and lvl_1[i][j] != 0:
                    if lvl_1[i][j] == '1':
                        block = BlockBricks(32, 32)
                        block.rect.x = j * 32  # координата x
                        block.rect.y = i * 32 + 24  # координата y
                        self.platforms.add(block)  # добавление в группу
                    elif lvl_1[i][j] == '6':
                        block = Pipe(32, 32)
                        pipe = (j, i - 2)
                        block.rect.x = j * 32  # координата x
                        block.rect.y = i * 32 + 24  # координата y
                        self.platforms.add(block)  # добавление в группу
                    elif lvl_1[i][j] == '9':
                        block = BlockBricks(0, 0)
                        block.rect.x = j * 32  # координата x
                        block.rect.y = i * 32 + 24  # координата y
                        self.platforms.add(block)  # добавление в группу
                    #  block.rect.x = j * 32  # координата x
                    #  block.rect.y = i * 32 + 24  # координата y
                    #  self.platforms.add(block)  # добавление в группу
                    # я хз почему не работает ошибка с колизией
                elif lvl_1[i][j] == '2':
                    cookie = (j, i - 1)
                    cok = Cookie(32, 32)
                    cok.rect.x = j * 32  # координата x
                    cok.rect.y = i * 32 + 24  # координата y
                    cookies.add(cok)  # добавление в группу
                elif lvl_1[i][j] == '3':
                    present = (j, i - 1)
                    pres = Presents(32, 32, presents)
                    pres.rect.x = j * 32  # координата x
                    pres.rect.y = i * 32 + 24  # координата y
                    presents.add(pres)  # добавление в группу


def check(coords):
    global coins, cookie, present, pipe
    cor = (coords[0] // 32, (coords[1] - 24) // 32)
    if cor == cookie:
        coins += 30
        cookies.remove(cookies)
    if cor == present:
        coins += 30
        presents.remove(presents)
    if cor == pipe:
        coins += 30
        racing()
    render_coins(coins)
    save_in_coins_txt(coins)


def render_coins(coins):
    conclusion = small_font.render(
        f'Количество очков: {coins}', True, 'black')
    screen.blit(conclusion, (100, 100))


def save_in_coins_txt(coins):  # сохранение очков в coins.txt
    with open('coins.txt', encoding='utf8', mode='w') as file:
        dump(coins, file)