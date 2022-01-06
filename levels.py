from race import racing
from load import load_image, load_level, screen
import pygame
from settings import small_font
from json import dump
cookies = pygame.sprite.Group()
presents = pygame.sprite.Group()
delete = False
delete1 = False
tasks = 0
flag_on_lvl2 = False
coins = 0


class BlockBricks(pygame.sprite.Sprite):  # класс для платформ
    image = load_image('brick.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров


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
        background = load_image('back_game3.png')  # задний фон
        screen.blit(background, (0, 0))
        self.platforms.draw(screen)  # платформы
        cookies.draw(screen)
        presents.draw(screen)

    def update(self):  # обновление экрана
        global cookies, delete, presents, delete1, tasks
        self.platforms.update()
        cookies.update()
        if delete:
            cookies.remove(cookies)
            delete = False
            tasks += 1
        if delete1:
            presents.remove(presents)
            delete1 = False
            tasks += 1
        if tasks == 2:
            block = Pipe(0, 0)
            block.rect.x = 770  # координата x
            block.rect.y = 82  # координата y
            self.platforms.add(block)  # добавление в группу
       


class DemoLevel1(Level):
    def __init__(self, player):
        global cookies, presents
        Level.__init__(self, player)  # наследуем игрока
        lvl_1 = load_level('level1.txt')
        for i in range(len(lvl_1)):
            for j in range(len(lvl_1[i])):
                if lvl_1[i][j] == '1':
                    block = BlockBricks(32, 32)
                    block.rect.x = j * 32  # координата x
                    block.rect.y = i * 32 + 24  # координата y
                    self.platforms.add(block)  # добавление в группу
                elif lvl_1[i][j] == '2':
                    cok = Cookie(32, 32)
                    cok.rect.x = j * 32  # координата x
                    cok.rect.y = i * 32 + 24  # координата y
                    cok.player = self.player
                    cookies.add(cok)  # добавление в группу
                elif lvl_1[i][j] == '3':
                    present = Presents(32, 32, presents)
                    present.rect.x = j * 32  # координата x
                    present.rect.y = i * 32 + 24  # координата y
                    presents.add(present)  # добавление в группу


def check(coords):
    global delete, delete1, tasks, coins
    if coords[0] // 32 == 2 and (coords[1] - 24) // 32 == 11:  # cookie
        coins += 30
        delete = True
    if coords[0] // 32 == 11 and (coords[1] - 24) // 32 == 11:  # present
        coins += 30
        delete1 = True
        print(len(presents.sprites()))
    if coords[0] == 773 and coords[1] == 32 and tasks == 2:
        coins += 30
        racing()
    render_coins(coins)
    save_in_coins_txt(coins)
    print(coords[0], coords[1])
    print(coins)

def render_coins(coins):
    conclusion = small_font.render(
        f'Количество очков: {coins}', True, 'black')
    screen.blit(conclusion, (100, 100))


def save_in_coins_txt(coins):  # сохранение очков в coins.txt
        with open('coins.txt', encoding='utf8', mode='w') as file:
            dump(coins, file)