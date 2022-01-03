import pygame
import sys
from player import Player, Camera
from levels import DemoLevel1, check  # уровни
from settings import terminate, scr_width, scr_height
from load import screen


def play():  # основная тестовая функция
    pygame.display.set_caption("1 уровень (бета)")  # название окна
    player = Player()  # создание игрока
    level_list = [DemoLevel1(player)]  # уровни (скоро будут новые)
    cur_level = level_list[0]  # выбор уровня
    active_session = pygame.sprite.Group()  # активная сессия
    player.level = cur_level
    player.rect.x = 0  # начальное положение игрока
    player.rect.y = 520
    active_session.add(player)
    running = True  # флаг для цикла
    clock = pygame.time.Clock()  # для скорости обновления экрана
    while running:  # основной цикл
        for event in pygame.event.get():  # следим за действиями играющего
            if event.type == pygame.QUIT:  # выход из игры
                terminate()
            if event.type == pygame.KEYDOWN:  # обработка клавиатуры
                if event.key == pygame.K_ESCAPE:
                    terminate()
                if event.key == pygame.K_UP:  # прыжок
                    player.jump()
                elif event.key == pygame.K_LEFT:  # влево
                    player.go_to_left()
                elif event.key == pygame.K_RIGHT:  # вправо
                    player.go_to_right()
            if event.type == pygame.KEYUP:  # если ничего не зажато
                if event.key == pygame.K_LEFT:
                    player.stop()  # остновка, если герой идёт влево
                elif event.key == pygame.K_RIGHT:
                    player.stop()  # остновка, если вправо
                elif event.key == pygame.K_e:
                    check(player.rect)
        active_session.update()  # обновление игрока
        cur_level.update()  # обновление уровня
        if player.rect.left < 0:  # ограничение движения за экран слева
            player.rect.left = 0
        if player.rect.right > scr_width:  # справа
            player.rect.right = scr_width
        cur_level.draw(screen)  # рисовка выбранного уровня
        active_session.draw(screen)
        clock.tick(30)  # fps
        pygame.display.flip()  # обновление экрана
    pygame.quit()  # закрытие игры