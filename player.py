import pygame
from load import load_image
pygame.init()  # инициализация для корректной работы функции загрузки - load_image
size = scr_width, scr_height = 800, 600  # размеры окна
screen = pygame.display.set_mode(size)


class Player(pygame.sprite.Sprite):  # класс главного героя
    # изображение главного героя
    image = load_image('santa2.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.right = True  # изначально герой повернут вправо
        self.hero_image = Player.image
        self.rect = self.hero_image.get_rect()  # размеры игрока
        self.rect.height = self.rect.height - 10  # делаем его ниже
        self.score_x = 0  # векторы скорости игрока
        self.score_y = 0

    def gravity(self):  # гравитация
        self.score_y += 0.9

        if self.score_y >= 0 and self.rect.y >= scr_height - self.rect.height:
            self.score_y = 0    # смена значения у на 0, при нахождении на "земле"
            self.rect.y = scr_height - self.rect.height

    def jump(self):  # прыжок
        self.rect.y += 10  # проверяем, есьб ли что над героем
        collide = pygame.sprite.spritecollide(
            self, self.level.platforms, False)  # проверка на коллизию
        self.rect.y -= 10  # возращение на "землю"
        if self.rect.bottom >= scr_height or len(collide) > 0:
            self.score_y = -16   # прыгаем, если ничего не мешает

    def go_to_left(self):  # движение игрока влево
        self.score_x = -10  # Двигаем игрока влево по Х
        if(self.right):  # проверка на то, куда он смотрит
            self.flip()  # если нужно, то переворачиваем
            self.right = False

    def go_to_right(self):  # движение игрока вправо
        self.score_x = 10  # Двигаем игрока вправо по Х
        if (not self.right):  # проверка на то, куда он смотрит
            self.flip()  # если нужно, то переворачиваем
            self.right = True

    def stop(self):  # остновка движения
        self.score_x = 0

    def update(self):  # передвижение игрока
        self.gravity()  # гравитация
        self.rect.y += self.score_y  # передвижение вверх или вниз
        blocks_collide = pygame.sprite.spritecollide(
            self, self.level.platforms, False)  # слежка за препятствиями по вертикали
        for block in blocks_collide:  # установка нужных сторон по вертикали
            if self.score_y > 0:  # если вверх
                self.rect.bottom = block.rect.top
            elif self.score_y < 0:  # если вниз
                self.rect.top = block.rect.bottom
            self.score_y = 0  # остановка движения
        self.rect.x += self.score_x  # передвижение вправо
        blocks_collide = pygame.sprite.spritecollide(
            self, self.level.platforms, False)  # слежка за препятствиями по горизонтали
        for block in blocks_collide:  # установка нужных сторон по горизонтали
            if self.score_x > 0:  # если вправо
                self.rect.right = block.rect.left
            elif self.score_x < 0:  # если влево
                self.rect.left = block.rect.right

    def flip(self):  # отражение изображения при поворте
        self.image = pygame.transform.flip(self.image, True, False)
