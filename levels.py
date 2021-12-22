from load import load_image
import pygame


class Platform(pygame.sprite.Sprite):  # класс для платформ
    image = load_image('platform.png')  # изображение платформы

    def __init__(self, width, height):
        super().__init__()
        self.rect = self.image.get_rect()  # установка размеров
        self.rect.height = self.rect.height - 20  # корректируем размеры
        self.rect.width = self.rect.width - 30


class Level(object):  # класс для уровня
    def __init__(self, player):
        self.player = player  # сам игрок
        self.platforms = pygame.sprite.Group()  # группа спрайтов

    def draw(self, screen):  # рисовка объектов
        background = load_image("background.png")  # задний фон
        screen.blit(background, (0, 0))
        self.platforms.draw(screen)  # платформы

    def update(self):  # обновление жкрана
        self.platforms.update()


class Level_1(Level):  # 1-ый уровень
    def __init__(self, player):
        Level.__init__(self, player)  # наследуем игрока
        level = [  # ширина, высота и координаты (х и y) платформ уровня
                [150, 32, 500, 500],
                [130, 32, 100, 400],
                [110, 32, 600, 300],
                [75, 32, 0, 260],
        ]
        for platform in level:  # добавление всех платформ в группу
            # создание объекта платформы со своей длиной и шириной
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]  # координата x
            block.rect.y = platform[3]  # координата y
            block.player = self.player
            self.platforms.add(block)  # добавление в группу