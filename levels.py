import sys
from race import game
from load import load_image
import pygame
from demo1 import lvl
cookies = pygame.sprite.Group()
presents = pygame.sprite.Group()
delete = False
delete1 = False
tasks = 0


class Platform(pygame.sprite.Sprite):  # класс для платформ
    image = load_image('platform.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.height = self.rect.height - 20  # корректируем размеры
        self.rect.width = self.rect.width - 30


class BlockBricks(pygame.sprite.Sprite):  # класс для платформ
    image = load_image('bricks_32.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров


class Cookie(pygame.sprite.Sprite):
    image = load_image('cookie.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width -= 32
        self.rect.height -= 32


class Presents(pygame.sprite.Sprite):
    image = load_image('present.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width -= 40
        self.rect.height -= 40


class Charcoal(pygame.sprite.Sprite):
    image = load_image('coal.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.width -= 40
        self.rect.height -= 40


class Truba(pygame.sprite.Sprite):
    image = load_image('pipe.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров


class Level(object):  # класс для уровня
    def __init__(self, player):
        self.player = player  # сам игрок
        self.platforms = pygame.sprite.Group()  # группа спрайтов

    def draw(self, screen):  # рисовка объектов
        global cookies
        background = load_image("back_game3.png")  # задний фон
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
            if tasks == 2:
                block = Truba(0, 0)
                block.rect.x = 20 * 32  # координата x
                block.rect.y = 17 * 32 + 24  # координата y
                block.player = self.player
                self.platforms.add(block)  # добавление в группу
        if delete1:
            presents.remove(presents)
            delete1 = False
            block = Charcoal(0, 0)
            block.rect.x = 11 * 32  # координата x
            block.rect.y = 11 * 32 + 24  # координата y
            block.player = self.player
            self.platforms.add(block)  # добавление в группу
            tasks += 1
            if tasks == 2:
                block = Truba(0, 0)
                block.rect.x = 20 * 32  # координата x
                block.rect.y = 17 * 32 + 24  # координата y
                block.player = self.player
                self.platforms.add(block)  # добавление в группу


class DemoLevel1(Level):
    def __init__(self, player):
        global cookies, presents
        Level.__init__(self, player)  # наследуем игрока

        for i in range(len(lvl)):
            for j in range(len(lvl[i])):
                xz = lvl[i][j]
                if xz == 2:
                    cok = Cookie(32, 32)
                    cok.rect.x = j * 32  # координата x
                    cok.rect.y = i * 32 + 24  # координата y
                    cok.player = self.player
                    cookies.add(cok)  # добавление в группу
                elif xz == 3:
                    pr = Presents(32, 32)
                    pr.rect.x = j * 32  # координата x
                    pr.rect.y = i * 32 + 24  # координата y
                    pr.player = self.player
                    presents.add(pr)  # добавление в группу
                elif xz != 0:
                    if xz == 1:
                        block = BlockBricks(32, 32)
                    block.rect.x = j * 32  # координата x
                    block.rect.y = i * 32 + 24  # координата y
                    block.player = self.player
                    self.platforms.add(block)  # добавление в группу


def check(coords):
    global delete, delete1, tasks
    if coords[0] // 32 == 2 and (coords[1] - 24) // 32 == 11:  # cookie
        delete = True
    if coords[0] // 32 == 11 and (coords[1] - 24) // 32 == 11:  # present
        delete1 = True
    if coords[0] // 32 == 20 and (coords[1] - 24) // 32 == 15 and tasks == 2:  # escape
        game()